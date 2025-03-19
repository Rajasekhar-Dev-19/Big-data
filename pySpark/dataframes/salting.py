"""
The Spark Web UI is the best native solution to identify the skewness in your Spark job.When you are at the Stages tab in Spark UI,
the skewed partitions hang within a stage and don’t seem to progress for a while on a few partitions.
If we look at the summary metrics, the max column usually has a much larger value than the medium and more records count.
Then we know we have encountered a data skew issue.

How to know which part of the code causes data skew?
The stage detail page in Spark UI only gives us a visual representation of the DAG.
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import IntegerType
from pyspark.sql.functions import spark_partition_id, rand

spark = SparkSession.builder.appName("Salting").getOrCreate()

df_evenly = spark.createDataFrame([i for i in range(1000000)], IntegerType()).repartition(3)
df_evenly = df_evenly.withColumn("partitionId", spark_partition_id())

# print(df_evenly.rdd.getNumPartitions())

# df_evenly.groupby([df_evenly.partitionId]).count().sort(df_evenly.partitionId).show()

# df_evenly.alias("left").join(df_evenly.alias("right"),"value", "inner").count()

df0 = spark.createDataFrame([0] * 999998, IntegerType()).repartition(1)
df1 = spark.createDataFrame([1], IntegerType()).repartition(1)
df2 = spark.createDataFrame([2], IntegerType()).repartition(1)
df_skew = df0.union(df1).union(df2)
df_skew = df_skew.withColumn("partitionId", spark_partition_id())
## If we apply the same function call again, we get what we want to see for the one partition with much more data than the other two.
df_skew.groupby([df_skew.partitionId]).count().sort(df_skew.partitionId).show()

"""
Data Skew causes slow performance in Spark, and a job is stuck in a few partitions that hang forever. 
There are multiple strategies to resolve a skew. Today, with Adaptive Query Execution (AQE) on Spark, 
it’s easier for Spark to be clever to figure out the optimized way. In edge cases, 
AQE isn’t 100% giving the best optimization. At those times, we still need to intervene and be familiar with which to use.

1. Leveraging the Number of Partitions
spark.sql.shuffle.partitions might be one of the most critical configurations in Spark. 
It configures the number of partitions to use when shuffling data for joins or aggregations. 
Configuring this value won’t always mean dealing with the skew issue, but it could be general optimization on the Spark job. 
The default value is 200, which is suitable for many big data projects back in the day and still relevant for small/medium size data projects. 

Think of this as the number of bins when data has to be tossed around during the shuffling stage. 
Are there too much data for a single bin to handle, or are they almost full?

2. Broadcast join
Broadcast join might be the fastest join type that you can use to avoid skewness. By giving when the BROADCAST hint, 
we explicitly provide information to Spark on which dataframe we’d need to send to each executor. 

The broadcast join usually works with smaller size dataframe like dimension tables or the data has metadata. 
It is not appropriate for transaction tables with millions of rows.
"""

# df_skew.join(broadcast(df_evenly.select("value")),"value", "inner").count()

"""
The SALT idea from cryptography introduced randomness to the key without knowing any context about the dataset. 
The idea is for a given hot key; if it combines with different random numbers, 
we’ll not have all the data for the given key processed in a single partition. 
A significant benefit of SALT is it is unrelated to any of the keys, 
and you don’t have to worry about some keys with similar contexts with the same value again.

The core idea of leveraging key salting is to think space-time tradeoff.

Add the salt key as part of the key as a new column. We also call the original key and the salt key a composite key. 
The newly added key forces Spark to hash the new key to a different hash value, so it shuffles to a different partition. 
Note we can also be dynamic to get the number of randomness on the salt key by retrieving the value from
"""

df_left = df_skew.withColumn("salt", (rand() * spark.conf.get("spark.sql.shuffle.partitions")).cast("int"))

df_left.show()