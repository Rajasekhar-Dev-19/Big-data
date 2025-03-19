from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, col

spark = SparkSession.builder.appName("Union and UnionByName").getOrCreate()

cardinal_file="F:\Bigdata\Datasets\cardinal_directions.txt"
ordinal_file="F:\Bigdata\Datasets\ordinal_directions.txt"

ordinal_df = spark.read.csv(ordinal_file,header=True,inferSchema=True)
cardinal_df = spark.read.csv(cardinal_file,header=True,inferSchema=True)
# ordinal_df.printSchema()
# cardinal_df.printSchema()
# ordinal_df.show()
# cardinal_df.show()
"""
Scenario-1 : Columns (Schema) are same but order is different, then union and UnionAll will give result as it is
But unionByName will thrown an error, if the column names are different, So we must have to rename the column names 
before going to use unionByName.

Scenario-2 : Columns (Schema) are different, in this situation union, unionAll and UnionByName will throw an error
We need to handle this situation by generating the dynamic columns with NULL values for missing columns on DF's using WithColumn Transformation
But, if columns names are same on both DataFrames and if DF's will have excess columns UnionByName will automatically 
populate the NULL in missing columns. without generating the another missing column on DF. 
"""

# card_df = cardinal_df.withColumn("dir_description",lit(None))
# ordinal_df = ordinal_df.select(ordinal_df.dir_id,ordinal_df.dir_name,ordinal_df.description)
# result_df = card_df.union(ordinal_df)
# result_df = cardinal_df.unionAll(ordinal_df)
# result_df = cardinal_df.unionByName(ordinal_df,allowMissingColumns=True)
# ordinal_df.show()
# result_df.show()
ordinal_df = ordinal_df.select(ordinal_df.dir_id.alias("id"),ordinal_df.dir_name.alias("name"))
ordinal_df.printSchema()
result = cardinal_df.union(ordinal_df)
# result.show()

