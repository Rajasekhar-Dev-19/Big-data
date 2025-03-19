"""
First we need to initialize the SparkSession using the builder pattern method
defined in the SparkSession class. while initializing we can provide optionally appName() and master() methods.
--> appName() : used to set Application name.
--> getOrCreate() : This returns a SparkSession object if already exists, and creates a new one if not exists.
Note: Creating SparkSession object, internally creates a one SparkContext per a JVM.
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Create RDD's").getOrCreate()
# spark = SparkSession.builder.getOrCreate()

# creating an empty RDD
rdd = spark.sparkContext.emptyRDD()
print(rdd)

# create an RDD using parallelize method.
data = [1,2,3,4,5,6,7,8,9,10] # local python list object.

"""
spark:
SparkContext :
parallelize : parallelize method will convert local object into spark RDD.
"""
parl_rdd = spark.sparkContext.parallelize(data)
print(parl_rdd.collect())

# create an RDD using textFile method.
"""
textFile : we can load local file/HDFS/Cloud file into an RDD.
"""
file_path = "C:/Users/sekha/OneDrive/Desktop/Bigdata/dept_data/dept_data.txt"
# file_rdd = spark.sparkContext.textFile("C:/Users/sekha/OneDrive/Desktop/Bigdata/dept_data/dept_data.txt")
""" or """
file_rdd = spark.sparkContext.textFile(file_path)
print(file_rdd.collect())

# create an RDD with partitions.
lst = [1,2,3,4,5,6,7,8,9,10]
"""
getNumPartitions : with help of getNumPartitions we can get the partition numbers on RDD's.
"""
rdd1 = spark.sparkContext.parallelize(lst,10)
print(rdd1.getNumPartitions())


