from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, isnull,col, when

spark = SparkSession.builder.appName("Union").getOrCreate()

"""
union, unionAll and unionByName
"""

# cardinal_path="F:\Bigdata\Datasets\cardinal_directions.txt"
# ordinal_path="F:\Bigdata\Datasets\ordinal_directions.txt"
#
# cardinal_df = spark.read.csv(cardinal_path,header=True,inferSchema=True)
# ordinal_df = spark.read.csv(ordinal_path,header=True,inferSchema=True)

# cardinal_df.show()
# ordinal_df.show()

# cardinal_df.printSchema()
# ordinal_df.printSchema()
#
# card_df = cardinal_df.withColumn("directions",lit(None))
# ord_df = ordinal_df.withColumn("desc",lit(None))
# cr_df = card_df.select(card_df.id,card_df.name,card_df.desc,card_df.directions)
# or_df = ord_df.select(ord_df.id,ord_df.name,ord_df.desc,ord_df.direcctions)
# cr_df.show()
# or_df.show()
#
# result_df = cr_df.union(or_df)
# result_df.show()

# result_df = cardinal_df.union(ordinal_df)
# result_df_1 = cardinal_df.unionAll(ordinal_df)
# result_df_2 = cardinal_df.unionByName(ordinal_df,allowMissingColumns=True)
# result_df.show()
# result_df_1.show()
# result_df_2.show()
#


file_path ="F:/Bigdata/Datasets/null_dataset.txt"

df = spark.read.csv(file_path,header=True,inferSchema=True)

# we can fill all columns with the nulls
null_df = df.na.replace("null",None)

filter_df = null_df.filter(isnull("dept_id"))
# filter_df.show()

# null_df = df.filter(col("dept_id") == 'null')
# null_df.show()
# drop_df = df.dropDuplicates(["dept_id","dept_name","dept_location"]).sort("dept_id","dept_location")
# drop_df.show()

# We can specify the specific columns to populate true nulls instead of hard coded nulls
# null_df = df.withColumn("dept_id",when(col("dept_id") == 'null',None).otherwise(col("dept_id")))\
#     .withColumn("dept_name",when(col("dept_name")=='null',None).otherwise(col("dept_name")))\
#     .withColumn("dept_location",when(col("dept_location")=='null',None).otherwise(col("dept_location")))
# null_df.show()

# filter_df = null_df.filter(col("dept_id") == "null")
# filter_df.show()

# filter_df = null_df.filter(isnull("dept_id"))
# filter_df.show()
#
# filter_df_1 = null_df.filter(isnull("dept_id") & isnull("dept_name"))
# filter_df_1.show()
# null_df.printSchema()
#
# fill_na_df = null_df.fillna(999)
# fill_na_df.show()

# drop_na_df = null_df.dropna(subset=["dept_id","dept_name"])
# drop_na_df.show()

# filter_df = null_df.filter(isnull("dept_id"))
# filter_df.show()

# JSON

file_path = "D:/Data/Zipcode_JSON/zipcodes.json"
json_df = spark.read.json(file_path)

# json_df.printSchema()
# json_df.show(5)

multi_json_file_path = "D:/Data/Hacathon_employees_json/mocked_data.json"
json_df_1 = spark.read.option("multiline",True).json(multi_json_file_path)
json_df_2 = spark.read.json(multi_json_file_path,multiLine=True)
json_df_3 = spark.read.format("json").option("multiline",True).load(multi_json_file_path)

json_df_3.printSchema()
# json_df_1.show()























