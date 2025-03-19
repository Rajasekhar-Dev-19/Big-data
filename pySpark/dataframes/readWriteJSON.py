"""
Reading JSON File
Reading from Multiline JSON file.
Reading Multiple files at a time
Reading all files in a folder
Using user specified schema
Reading file using PysparkSQL
Writing DataFrame to JSON File
"""

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("JSON").getOrCreate()
#Reading JSON File
file_path='D:/Data/Zipcode_JSON/zipcodes.json'
way_1 = spark.read.json(file_path)  # it will automatically infer the Schema & Creates a dataframe from the JSON.
# way_1.printSchema()
# json_df.show(5)
way_2 = spark.read.format('json').load(file_path)
# way_2.printSchema()
# way_2.show()

# Multiline
file_path_1 = "D:/Data/Hacathon_employees_json/mocked_data.json"
way_1_1 = spark.read.option("multiline",True).json(file_path_1)
way_1_1.printSchema()
way_1_1.show()

# Read Multiple specific files at a time
mul_json_df = spark.read.json(['file_1','file_2','file_n'])
# Read all files from a folder
all_json_df = spark.read.json('directory_path/resources/*.json')

# Read JSON file with custom schema
# custom_schema_json_df = spark.read.schema(custom_schema).json(file_path)