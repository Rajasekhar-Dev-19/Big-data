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

raw_df.filter(col("gender") == 'Male').show()
# need to convert a dataframe into a table
raw_df.createOrReplaceTempView("emp")
query = "select * from emp WHERE gender = 'Female' and salary >= 30000"
df = spark.sql(query)
df.show()