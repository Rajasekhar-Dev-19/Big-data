from pyspark.sql import SparkSession
from pyspark.sql.functions import ntile, lag, lead, col, max, min, sum, avg, count, row_number, rank, dense_rank, desc, percent_rank, cume_dist, first, last, nth_value
from pyspark.sql import Window
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
spark = SparkSession.builder.appName("Windowing Functions").getOrCreate()

# get the running total
bank_data = [(101,10000,'01-01-2025'),(101,5000,'01-02-2025'),(101,40000,'01-05-2025'), (101,50000,'01-18-2025'),
 (101,1000,'01-20-2025'), (101,80000,'01-03-2025'), (101,90000,'01-26-2025'),(101,120000,'01-31-2025')
]

bank_schema = ["cust_id","amount","date"]
input_df = spark.createDataFrame(bank_data,bank_schema)
# input_df.show()
#
# running_total = input_df.withColumn("r_total",sum("amount").over(Window.partitionBy("cust_id").orderBy("date")))\
#                         .withColumn("r_avg",avg("amount").over(Window.partitionBy("cust_id").orderBy("date")))
# running_total.show()

# lead, lag, first value, last value

# get the salary difference
emp_data = [(101,25000,'01-01-2015'),(101,32000,'01-01-2016'),(101,40000,'01-01-2017'), (101,50000,'01-01-2018'),
 (101,65000,'01-01-2019'), (101,80000,'01-01-2020'), (101,90000,'01-01-2021'),(101,120000,'01-01-2022')
]

cust_schema = ["id","salary","date"]
input_df = spark.createDataFrame(emp_data,cust_schema)
# input_df.show()

emp_f_l_path = "D:/Data/Employee/emp_first_last_win_val_data.txt"
emp_input_df = spark.read.csv(emp_f_l_path, header=True, inferSchema=True)
emp_input_df.show()

f_df = emp_input_df.withColumn("first_hire_date",first("hire_date").over(Window.partitionBy("dept_id").orderBy("hire_date")))
# f_df.show()

l_df = f_df.withColumn("last_hire_date",last("hire_date").over(Window.partitionBy("dept_id").orderBy("hire_date").rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing)))
# l_df.show()

tile_df = emp_input_df.withColumn("n_tile",ntile(4).over(Window.orderBy("dept_id")))
tile_df.show()

nth_df = emp_input_df.withColumn("n_th_val",nth_value("salary",2).over(Window.orderBy(desc("salary")).rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing)))
# nth_df.show()


# first_value_df = input_df.withColumn("f_val", first("salary").over(Window.partitionBy("id").orderBy("date")))
# first_value_df.show()

# res_df= input_df.withColumn("prev_year_sal",lag("salary").over(Window.partitionBy("id").orderBy("date"))) \
#                 .withColumn("next_year_sal",lead("salary").over(Window.partitionBy("id").orderBy("date")))
# res_df.show()
#
# res_df_1 = res_df.withColumn("lag_incre_sal",col("salary") - col("prev_year_sal")) \
#                 .withColumn("lead_incre_sal",col("next_year_sal") - col("salary"))
# res_df_1.show()

# res_df = input_df.withColumn("next_year_sal",lead("salary").over(Window.partitionBy("id").orderBy("date")))
# # res_df.show()
# res_df_1 = res_df.withColumn("incre_sal",col("next_year_sal") - col("salary") )
# res_df_1.show()

# first_val = input_df.withColumn("f_val",first("salary").over(Window.partitionBy("id").orderBy("date")))
# first_val.show()
# last_val = input_df.withColumn("f_val",last("salary").over(Window.partitionBy("id").orderBy("date").rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing)))
# last_val.show()

# file_path = "F:/Bigdata/Datasets/emp_window_functions.txt"
# emp_schema = StructType([
#     StructField("dept_id",IntegerType()),
#     StructField("emp_name",StringType()),
#     StructField("age",IntegerType()),
#     StructField("gender",StringType()),
#     StructField("salary",IntegerType())
# ])
#
# raw_df = spark.read.csv(file_path,schema=emp_schema)
# # raw_df.orderBy("dept_id").show()
# # get the maximum salary
# # raw_df.select(min("salary").alias("max_salary")).show()
#
# df = raw_df.withColumn("row_num",row_number().over(Window.orderBy(desc("salary"))))\
#     .withColumn("rnk",rank().over(Window.orderBy(desc("salary"))))\
#     .withColumn("d_nrnk",dense_rank().over(Window.orderBy(desc("salary")))) \
#     .withColumn("p_rank",percent_rank().over(Window.orderBy(desc("salary"))))
#     # .show()
# # df.show()
# print(df.orderBy("row_num").show())
# df.filter(col("dnrnk") == 4).show()

