"""
Similar to SQL GROUP BY clause, PySpark groupBy() transformation that is used to group rows that have the same values
in specified columns into summary rows. It allows you to perform aggregate functions on groups of rows,
rather than on individual rows, enabling you to summarize data and generate aggregate statistics.
on top of groupBy transformation we can apply bellow aggregate functions
--> count()
--> max()
--> min()
--> mean()
--> sum()
--> avg()
--> agg()
--> pivot()
"""
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType
from pyspark.sql.functions import sum, avg, min, max, count
import pyspark.sql.functions

emp_file_path = "C:/Users/sekha/OneDrive/Desktop/Bigdata/emp_data/emp_data.txt"
dept_file_path = "C:/Users/sekha/OneDrive/Desktop/Bigdata/dept_data/dept_data.txt"

emp_schema = StructType([
    StructField("emp_id",IntegerType()),
    StructField("dept_id",IntegerType()),
    StructField("emp_name",StringType()),
    StructField("age",IntegerType()),
    StructField("gender",StringType()),
    StructField("salary",IntegerType())
])

dept_schema = (StructType().add("dept_id",IntegerType())
                           .add("dept_name",StringType())
                           .add("dept_location",StringType()))

spark = SparkSession.builder.appName("GroupBy").getOrCreate()

emp_df = spark.read.format("csv").options(inferSchema=True).schema(emp_schema).load(emp_file_path)
dept_df = spark.read.format("csv").options(inferSchema=True).schema(dept_schema).load(dept_file_path)

emp_df.show()
dept_df.show()

# join
join_df = emp_df.join(dept_df, emp_df.dept_id == dept_df.dept_id,"inner").sort("emp_id")

# join_df.printSchema()
# join_df.show()

join_df.groupBy("dept_name").count().withColumnRenamed("count","cnt").show()

# all aggregate function in a single go
group_df = join_df.groupBy("dept_name").agg(sum("salary").alias("sum_salary"),
                                            avg("salary").alias("avg_salary"),
                                            min("salary").alias("min_salary"),
                                            max("salary").alias("max_salary"),
                                            count("*").alias("cnt")
                                            )

# group_df.show(.)
