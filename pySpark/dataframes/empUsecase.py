from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Employee").getOrCreate()

file_path = "D:/Data/Employee/employee_records.csv"

raw_df = spark.read.csv(file_path,header=True, inferSchema=True)
raw_df.printSchema()

# print(raw_df.count())

raw_df.select("Joining_Date").distinct().show()