"""
row_number(): Assigns a sequential number to each row within a window.
rank(): Assigns a rank to each row within a window, with ties sharing the same rank.
dense_rank(): Assigns a dense rank to each row within a window, with no gaps in the ranks.
percent_rank(): Calculates the percentile rank of a row within a window.
cume_dist(): Calculates the cumulative distribution of a row within a window.
ntile() :
lag(): Accesses the value of a column from a preceding row within a window.
lead(): Accesses the value of a column from a following row within a window.
sum(): Calculates the sum of values within a window.
avg(): Calculates the average of values within a window.
min(): Finds the minimum value within a window.
max(): Finds the maximum value within a window.

"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import max, min, sum, avg, count, rank, dense_rank, desc, percent_rank, cume_dist, first, last, nth_value
from pyspark.sql import Window

spark = SparkSession.builder.appName("Aggregate Functions").getOrCreate()

# data = [("James", "Sales", 3000),
#     ("Michael", "Sales", 4600),
#     ("Robert", "Sales", 4100),
#     ("Maria", "Finance", 3900),
#     ("James", "Sales", 3000),
#     ("Scott", "Finance", 3300),
#     ("Jen", "Finance", 3900),
#     ("Jeff", "Marketing", 3000),
#     ("Kumar", "Marketing", 2000),
#     ("Saif", "Sales", 4600),
#     ("David", "Finance", 4000),
#   ]
# schema = ["employee_name", "department", "salary"]
# df = spark.createDataFrame(data=data, schema = schema)
#
# #  get the Nth Highest Salary
#
# rank_df = df.withColumn("rank",dense_rank().over(Window.orderBy(desc("salary"))))
# rank_df.show()
# result = rank_df.filter(rank_df.rank == 4)
# result.show()

from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql import Window
from pyspark.sql.functions import row_number, lead, lag, ntile, col

file_path = "F:/Bigdata/Datasets/emp_window_functions.txt"
emp_schema = StructType([
    StructField("emp_id",IntegerType()),
    StructField("emp_name",StringType()),
    StructField("age",IntegerType()),
    StructField("gender",StringType()),
    StructField("salary",IntegerType())
])

raw_df = spark.read.csv(file_path,schema=emp_schema)
raw_df.show()

df = raw_df.withColumn("s_rnm",row_number().over(Window.partitionBy("emp_id").orderBy(desc("salary")))) \
.withColumn("lst_val",last("salary").over(Window.partitionBy("emp_id").orderBy("salary").rowsBetween(Window.unboundedPreceding,Window.unboundedFollowing)))
# .withColumn("previous_sal",lag("salary").over(Window.partitionBy("emp_id").orderBy("salary"))) \


# .withColumn("hike",(((col("salary") - lag("salary").over(Window.partitionBy("emp_id").orderBy("salary")))/col("salary"))*100)) \
# .withColumn("lst_vl",last("salary").over(Window.partitionBy("emp_id").orderBy(desc("salary")).rowsBetween(1,3))) \
# .withColumn("lag_sal",lag("salary").over(Window.partitionBy("emp_id").orderBy(desc("salary")))) \
# .withColumn("s_rnk",rank().over(Window.partitionBy("emp_id").orderBy(desc("salary")))) \
# .withColumn("s_drnk",dense_rank().over(Window.partitionBy("emp_id").orderBy(desc("salary")))) \
# .withColumn("s_prnk",percent_rank().over(Window.partitionBy("emp_id").orderBy("salary"))) \
# .withColumn("ntile",ntile(10).over(Window.partitionBy("emp_id").orderBy("salary"))) \
# .withColumn("frst_vl",first("salary").over(Window.partitionBy("emp_id").orderBy(desc("salary")))) \


# .withColumn("cume_dist_sal",cume_dist().over(Window.partitionBy("emp_id").orderBy("salary"))) \

# df.filter(df.sal_rownum == 3).show()
# df.withColumn("hike",(((col("salary") - col("previous_sal"))/col("salary"))*100)).show()



# raw_df.sort("emp_id").show()

# df = raw_df.withColumn("salary_num",row_number().over(Window.partitionBy("emp_id").orderBy(desc("salary"))))
# df.show()