from pyspark.sql import SparkSession
from pyspark.sql.types import StructField, StructType, StringType, IntegerType

spark = SparkSession.builder.appName("Creating Dataframes").getOrCreate()

"""
A DataFrame is the most common Structured API and simply represents a table of data with rows and columns. The
list of columns and the types in those columns the schema.

Spark has several core abstractions: Datasets, DataFrames, SQL Tables, and Resilient Distributed Datasets (RDDs).
These abstractions all represent distributed collections of data however they have different interfaces for working
with that data. The easiest and most efficient are DataFrames, which are available in all languages.
"""

# Create a Dataframe with createDataFrame method
# Way-1
Employee = spark.createDataFrame([
('1', 'Joe', '70000', '1'),
('2', 'Henry', '80000', '2'),
('3', 'Sam', '60000', '2'),
('4', 'Max', '90000', '1')],
['Id', 'Name', 'Salary','DepartmentId']
)

# Way-2
data = [
('1', 'Joe', '70000', '1'),
('2', 'Henry', '80000', '2'),
('3', 'Sam', '60000', '2'),
('4', 'Max', '90000', '1')
]
schema = ['Id', 'Name', 'Salary','DepartmentId']
Employee = spark.createDataFrame(data,schema)
# Employee.show()

# convert an RDD into Dataframe with toDF method
rdd = spark.sparkContext.parallelize(data)
# print("Type:",rdd)
# print(rdd.collect())
# converting an RDD into a dataFrame
df = rdd.toDF(schema)
# print("Type:",df)
# df.printSchema()

# Provide custom schema to a dataframe
"""
StringType: Represents strings of characters.
IntegerType: Represents whole numbers (integers).
FloatType: Represents decimal numbers (floating point).
DoubleType: Represents double-precision decimal numbers.
BooleanType: Represents boolean values (True or False).
DateType: Represents a date without a time component.
TimestampType: Represents a timestamp with both date and time.
ArrayType: Represents an array of elements with the same data type.
MapType: Represents a map or dictionary with key-value pairs.
StructType: Represents a structure or nested columns within a DataFrame.
"""

data1 = [
(1, 'Joe', 70000, 1),
(2, 'Henry', 80000, 2),
(3, 'Sam', 60000, 2),
(4, 'Max', 90000, 1)
]
schema1 = StructType([
  StructField('Id', IntegerType(), True),
  StructField('Name', StringType(), True),
  StructField('Salary', IntegerType(), True),
  StructField('DepartmentId', IntegerType(), True)
  ])

# df = spark.createDataFrame(data1,schema1)
# df.printSchema()
# df.show()

data_x = ["ant","bat","cat","dog","bat","ant","cat","dog","cat","bat","ant","dog","dog","cat","bat","ant","Lion","ant"]

input_df = spark.createDataFrame(data_x)
input_df.show()