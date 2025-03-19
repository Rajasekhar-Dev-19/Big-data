from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import sum, count, max, min, avg, col
spark = SparkSession.builder.appName("Aggregation Functions").getOrCreate()

file_path = "F:/Bigdata/Datasets/emp.txt"

emp_schema = StructType([
    StructField("emp_id",IntegerType()),
    StructField("emp_name",StringType()),
    StructField("age",IntegerType()),
    StructField("gender",StringType()),
    StructField("salary",IntegerType())
])

raw_df = spark.read.csv(file_path,schema=emp_schema)
# raw_df.show()
# raw_df.select(sum("salary").alias("total_salary")).show()
# raw_df.select(count("salary").alias("count")).show()
# raw_df.select(max("salary").alias("max_salary")).show()
# raw_df.select(min("salary").alias("min_salary")).show()
# raw_df.select(avg("salary").alias("avg_salary")).show()
# raw_df.show()
# raw_df.show()

# raw_df.agg(sum("salary").alias("total_salary"),
#            max("salary").alias("max_salary"),
#            min("salary").alias("min_salary"),
#            avg("salary").alias("avg_salary"),
#            count("salary").alias("count")
#            ).show()
#
# raw_df.groupBy("gender").agg(sum("salary").alias("total_salary"),
#            max("salary").alias("max_salary"),
#            min("salary").alias("min_salary"),
#            avg("salary").alias("avg_salary"),
#            count("salary").alias("count")
#            ).show()

raw_df.filter(col("gender") == 'Male').show()
# need to convert a dataframe into a table
raw_df.createOrReplaceTempView("emp")
query = "select * from emp WHERE gender = 'Female' and salary >= 30000"
df = spark.sql(query)
df.show()