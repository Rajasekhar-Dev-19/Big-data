from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CrimeScenarios").getOrCreate()

file_path = "F:/Bigdata/Datasets/crime_data_since_2010.txt"

raw_df = spark.read.csv(file_path,header=True,inferSchema=True,sep="\t")
# raw_df.printSchema()
print(raw_df.count())
# raw_df.show(truncate=False)