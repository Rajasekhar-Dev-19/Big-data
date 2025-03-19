from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("RDD Transformations and Actions").getOrCreate()
print(spark) # it will bring the SparkSession Object location.