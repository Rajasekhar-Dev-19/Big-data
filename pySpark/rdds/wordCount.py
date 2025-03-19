from pyspark import SparkContext
sc = SparkContext.getOrCreate()

# read data from the Python local object
# reading data from a list
#
# input_rdd = sc.parallelize(data)
# map_rdd = input_rdd.map(lambda x:(x,1))
# result = map_rdd.reduceByKey(lambda x,y: x+y).sortBy(lambda x:x[1],ascending=False)

# reading data from a Nested list
# data_1 =[["ant","bat","cat","dog"],["bat","ant","cat","dog"],["cat","bat","ant","dog"],["dog","cat","bat","ant"],["Lion","ant"]]
#
# rdd = sc.parallelize(data_1)
# flat_rdd = rdd.flatMap(lambda x : x)
# map_rdd = flat_rdd.map(lambda x:(x,1))
# result_df = map_rdd.reduceByKey(lambda x,y:x+y).sortByKey(ascending=False)

data_2 =[["ant,bat,cat,dog"],["bat,ant,cat,dog"],["cat,bat,ant,dog"],["dog,cat,bat,ant"],["Lion,ant"]]
input_rdd = sc.parallelize(data_2)

# print(input_rdd)

input = [["Python",["Maths","Physics","Chemistry"]]]
# input_rdd = sc.parallelize(input)
# # print(input_rdd.collect())
# flat_rdd = input_rdd.flatMap(lambda x : [(x[0], subject) for subject in x[1]])
# print(flat_rdd.collect())

# input_1 = [('Python', 'Maths'), ('Python', 'Physics'), ('Python', 'Chemistry')]
# input_rdd = sc.parallelize(input)
# group_rdd = input_rdd.groupByKey()
# result = group_rdd.map(lambda x :[x[0],list(x[1])])
# print(result.collect())



# res = input_rdd.collect()
# print(type(input_rdd)) # RDD
# print(type(res)) # Python Local Object
# print(type(result))
# print(result_df.collect())


# read data from a file
# input_rdd = sc.textFile("F:/Bigdata/Datasets/animals.txt")
# print(input_rdd.collect())
# words_rdd = input_rdd.flatMap(lambda line:line.split(","))
# print(words_rdd.collect())
# words = words_rdd.map(lambda word:(word,1))
# print(words.collect())
# word_count = words.reduceByKey(lambda x,y:x+y)
# print(word_count.collect())

