"""
Joins :
1) Inner
2)left or leftouter or left_outer
3)right or rightouter or right_outer
4)full or full_outer 
5)left_semi and left_anti
6) cross join
"""
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Joins").getOrCreate()

data = [1,1,2,3,4,5]
data1 = ['1','1','2','3',None,None,'']
data2 = ['1','1','1','5',None,None,None]

df_1 = spark.createDataFrame(data1,"string").toDF("id")
df_2 = spark.createDataFrame(data2,"string").toDF("id")
# df_1.show()
# df_2.show()

inner_df = df_1.join(df_2, df_1.id == df_2.id,"inner")
# inner_df.show()
left_join_df = df_1.join(df_2, df_1.id == df_2.id,"left")
left_join_df = df_1.join(df_2, df_1.id == df_2.id,"leftouter")
left_join_df = df_1.join(df_2, df_1.id == df_2.id,"left_outer")
# left_join_df.show()

inner_df = df_1.join(df_2, df_1.id == df_2.id)
inner_df.show()
