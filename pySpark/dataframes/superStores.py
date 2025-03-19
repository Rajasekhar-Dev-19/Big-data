from pyspark.sql import SparkSession
from pyspark.sql.functions import col

file_path = "F:/Bigdata/Datasets/Super Stores/superstore.csv"

spark = SparkSession.builder.appName("Superstore Usecases").getOrCreate()

"""
step-1: load the data into a dataframe properly and make sure column names must without spaces, \
incase if we have spaces we need to rename them as meaningful column names.
 
"""

raw_df = spark.read.csv(file_path,header=True,inferSchema=True)
# raw_df.printSchema()
# print(raw_df.count())
# renaming the column names
input_df = raw_df.withColumnRenamed("Row ID","row_id") \
    .withColumnRenamed("Order ID","order_id") \
    .withColumnRenamed("Order Date","order_date") \
    .withColumnRenamed("Ship Date","ship_date") \
    .withColumnRenamed("Ship Mode","ship_mode") \
    .withColumnRenamed("Customer ID","customer_id") \
    .withColumnRenamed("Customer Name","customer_name") \
    .withColumnRenamed("Country/Region" , "country") \
    .withColumnRenamed("State/Province","state") \
    .withColumnRenamed("Postal Code","postal_code") \
    .withColumnRenamed("Product ID","product_id") \
    .withColumnRenamed("Sub-Category","sub_category") \
    .withColumnRenamed("Product Name","product_name")

# input_df.printSchema()

states_df = input_df.select("state").distinct().orderBy("state")
states_df.limit(100).show(truncate=False)