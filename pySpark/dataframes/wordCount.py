from pyspark.sql import SparkSession
from pyspark import SparkContext
from pyspark.sql.functions import explode,split,col

spark = SparkSession.builder.appName("Word Count").getOrCreate()

#

# Basic
# input_df = spark.read.text("F:/Bigdata/Datasets/animals.txt")
# print("Type --> ", type(input_df))
# word_df =  input_df.withColumn("word",explode(split(col("value"),",")))
# print("Type --> ", type(word_df))
# # group_df = word_df.groupBy("word").count()
# group_df = word_df.groupBy("word").count()
# print("Type --> ", type(group_df))
# # sort_df = group_df.sort("word")
# print("Type --> ", type(sort_df)

# # group_df.show()

# advanced
# res = input_df.withColumn("word",explode(split(col("value"),","))).groupBy("word").count().sort("word")
# res.show()
file_path="F:/Bigdata/Datasets/animals.txt"
input_df = spark.read.text(file_path)
flat_df = input_df.select(explode(split(input_df.value,",")).alias("word"))
word_cnt_df = flat_df.groupBy("word").count().orderBy("word",ascending=False)
word_cnt_df.show()

sc = SparkContext.getOrCreate()
data =[["ant","bat","cat","dog"],["bat","ant","cat","dog"],["cat","bat","ant","dog"],["dog","cat","bat","ant"],["Lion","ant"]]
rdd = sc.parallelize(data)
# print(rdd.collect())
flat_rdd = rdd.flatMap(lambda word:word)
# print(flat_rdd.collect())
# df = flat_rdd.toDF(["name"])
# df.show()