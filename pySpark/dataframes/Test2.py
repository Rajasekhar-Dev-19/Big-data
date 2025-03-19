from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum, max, min, avg, desc, isnull, lit, collect_list
spark = SparkSession.builder.appName("Group By").getOrCreate()

"""
Pivot
"""

subject_filepath = "D:/Data/Df Pivot Data/pivot_data.txt"

subject_df = spark.read.csv(subject_filepath, header=True, inferSchema=True)
# subject_df.show()

new_sub_df = subject_df.groupBy("id","name").agg(collect_list("subject").alias("subject"))
# new_sub_df.show(truncate=False)

final_df = new_sub_df.select(col("id"),col("name"),col("subject")[0].alias("sub1") \
                            ,col("subject")[1].alias("sub2") \
                            ,col("subject")[2].alias("sub3")
)

# final_df.show()

pivot_filepath = "D:/Data/Df Pivot Data/pivot_data_2.txt"

country_df = spark.read.csv(pivot_filepath, header=True, inferSchema=True)
# country_df.show()

final_df = country_df.groupBy("product").pivot("country").sum("amount")

# final_df.show()

"""
union, unionAll, unionByName
"""

# card_file_path = 'F:/Bigdata/Datasets/cardinal_directions.txt'
# ord_file_path = 'F:/Bigdata/Datasets/ordinal_directions.txt'
#
# card_df = spark.read.csv(card_file_path, header=True, inferSchema=True)
# ord_df = spark.read.csv(ord_file_path, header=True, inferSchema=True)
#
# # card_df.printSchema()
# # ord_df.printSchema()
#
# card_df.show()
# ord_df.show()
# new_ord_df = ord_df.withColumnRenamed("ord_name", "name").withColumnRenamed("ord_id","id")\
#     .select("id","name")
#
#
# card_df.unionAll(new_ord_df).show()
# new_ord_df.show()
# new_ord_df_1 = new_ord_df.select("id","name").withColumn("description",lit(None))
# new_ord_df_1.show()
# union_df = card_df.union(new_ord_df_1)
# union_df.show()

# unionall_df = card_df.unionAll(ord_df)
# unionall_df.show()

# unionb_df = card_df.unionByName(new_ord_df, allowMissingColumns=True)
# unionb_df.show()

emp_file_path="D:/Data/Employee/emp_for_joins.txt"
dept_file_path="D:/Data/Department/department_with_header.txt"
#
emp_df = spark.read.csv(emp_file_path, header=True, inferSchema=True,nullValue='NA')
dept_df = spark.read.csv(dept_file_path, header=True, inferSchema=True,nullValue='NA')

# emp_df.printSchema()
# dept_df.printSchema()

emp_df.show()
dept_df.show()
#
# # result = emp_df.filter(isnull(col("emp_id"))).show()
#
inner_join_df = emp_df.join(dept_df, emp_df.dept_id == dept_df.id,"inner")
# # join_df = emp_df.crossJoin(dept_df)
inner_join_df.show(50)
# # print(join_df.count())
# inner_join_df.show(50)
# semi_df = emp_df.join(dept_df, emp_df.emp_id == dept_df.id,"left_anti")
# semi_df.show(50)

# file_path="D:/Data/Employee/emp_with_header.txt"
# input_df = spark.read.csv(file_path,header=True,inferSchema=True)
# input_df.printSchema()
# input_df.select(max(input_df.salary).alias("max_salary")).show()
# input_df.select(min(input_df.salary).alias("min_salary")).show()
# input_df.select(sum(input_df.salary).alias("total_salary")).show()
# input_df.select(avg(input_df.salary).alias("avg_salary")).show()
# input_df.select(count(input_df.salary).alias("count")).show()
#
inner_join_df.groupBy("dept_id").agg(sum("salary").alias("total_salary"),
     avg("salary").alias("avg_salary"),
     max("salary").alias("max_salary"),
     min("salary").alias("min_salary"),
     count("*").alias("number_of_records")
).sort("dept_id",ascending=False).show()
# # input_df.select(min("salary")).show()
# # input_df.groupBy(col("dept_id")).agg(sum("salary").alias("total_salary")).orderBy(col("dept_id")).show()
#
# # input_df.show()
