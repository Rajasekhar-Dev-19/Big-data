from pyspark.sql import SparkSession
from pyspark.sql.functions import max, min, sum, avg, count, round

spark = SparkSession.builder.appName("Aggregate Functions").getOrCreate()

data = [("James", "Sales", 3000),
    ("Michael", "Sales", 4600),
    ("Robert", "Sales", 4100),
    ("Maria", "Finance", 3900),
    ("James", "Sales", 3000),
    ("Scott", "Finance", 3300),
    ("Jen", "Finance", 3900),
    ("Jeff", "Marketing", 3000),
    ("Kumar", "Marketing", 2000),
    ("Saif", "Sales", 4600),
    ("David", "Finance", 4000),
  ]
schema = ["employee_name", "department", "salary"]
df = spark.createDataFrame(data=data, schema = schema)
# df.printSchema()

# df.select(max("salary").alias("max_salary")).show()
# df.select(min("salary").alias("min_salary")).show()
# df.select(sum("salary").alias("total_salary")).show()
# df.select(avg("salary").alias("avg_salary")).show()
# df.select(count("*").alias("cnt")).show()

# df.select(max("salary").alias("max_salary")).select(min("salary").alias("min_salary")).show()
# error chaining select will not work
# Way-2
# df.agg(max("salary").alias("max_salary")).show()

# getting all the statistics in a single shot, then we need to use agg transformation
# df.agg(max("salary").alias("max_salary"),
#               min("salary").alias("min_salary"),
#               sum("salary").alias("total_salary"),
#               round(avg("salary"),2).alias("avg_salary"),
#               count("salary").alias("total_count")).show()



