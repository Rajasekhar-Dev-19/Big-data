"""
The pivot function is used to reshape a DataFrame by transforming unique values from one column into multiple columns,
allowing for better data analysis and visualization.
It typically requires an aggregation function to summarize the data after the pivot operation.
"""

from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import collect_list, col, row_number
spark = SparkSession.builder.appName("Pivot and Unpivot").getOrCreate()

data = [("Banana",1000,"USA"), ("Carrots",1500,"USA"), ("Beans",1600,"USA"), \
      ("Orange",2000,"USA"),("Orange",2000,"USA"),("Banana",400,"China"), \
      ("Carrots",1200,"China"),("Beans",1500,"China"),("Orange",4000,"China"), \
      ("Banana",2000,"Canada"),("Carrots",2000,"Canada"),("Beans",2000,"Mexico")]

columns= ["Product","Amount","Country"]
df = spark.createDataFrame(data = data, schema = columns)
# df.printSchema()
# df.show(truncate=False)
# pivotDF = df.groupBy("Product").pivot("Country").sum("amount")
pivotDF = df.groupBy("Country").pivot("Product").sum("amount")
# pivotDF.show()


data_v1 = [(101, "Python", "Maths"), (101, "Python", "Physics"), (101, "Python", "Chemistry")
,(102,'Scala','History'),(102,'Scala','Economics'),(102,'Scala','Civics')
           ,(103,'Java',"Maths"),(103,"Java","Chemistry")]
columns_v1 = ["s_id", "s_name", "subject"]
# Loading Local object data into a Spark Dataframe
df1 = spark.createDataFrame(data=data_v1,schema=columns_v1)
# df1.show()
# Group by s_id and s_name, and collect subjects into a list
# Way-1
grouped_df = df1.groupBy("s_id", "s_name").agg(collect_list("subject").alias("subject"))
grouped_df.show(truncate=False)
result_df = grouped_df.select(col("s_id"),col("s_name")
                              ,col("subject")[0].alias("s1") \
                              ,col("subject")[1].alias("s2") \
                              ,col("subject")[2].alias("s3")
                              )
# result_df.show()
#Create spark session

# Way-2:
# Add a row number to each subject for each student
window_spec = Window.partitionBy("s_id", "s_name").orderBy("subject")
df_with_row_num = df1.withColumn("row_num", row_number().over(window_spec))
df_with_row_num.show()
# Pivot the DataFrame
pivoted_df = df_with_row_num.groupBy("s_id", "s_name").pivot("row_num").agg({"subject":"first"})
pivoted_df.show()
result_df = pivoted_df.select(col("s_id"),col("s_name") \
                              ,col("1").alias("s1") \
                              ,col("2").alias("s2") \
                              ,col("3").alias("s3")
                              )
result_df.show()


