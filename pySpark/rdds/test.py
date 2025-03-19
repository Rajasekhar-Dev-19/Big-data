# Spark Session
from pyspark import SparkContext
sc = SparkContext.getOrCreate()

file_path = "C:/Users/sekha/OneDrive/Desktop/sample.txt"
input_rdd_1 = sc.textFile(file_path)
print(input_rdd_1.collect())
print(input_rdd_1.count())
flat_rdd = input_rdd_1.flatMap(lambda x:x.split(","))
print(flat_rdd.collect())
print(flat_rdd.count())
map_rdd = flat_rdd.map(lambda x:(x,1))
print(map_rdd.collect())
print(map_rdd.count())
result_rdd = map_rdd.reduceByKey(lambda x,y:x+y).sortByKey()
print(result_rdd.collect())
print(result_rdd.count())
# print(sc)
