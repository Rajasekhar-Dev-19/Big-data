
# print(0.1+0.2 == 0.3) # will return false

# windowing functions on Pyspark Dataframes

from pyspark.sql import SparkSession  # We have to import
from pyspark.sql import Window, functions
from pyspark.sql.functions import row_number,desc
spark = SparkSession.builder.appName('Window Functions').getOrCreate()


sampleData = (("James", "Sales", 3000), \
    ("Michael", "Sales", 4600),  \
    ("Robert", "Sales", 4100),   \
    ("Maria", "Finance", 3000),  \
    ("James", "Sales", 3000),    \
    ("Scott", "Finance", 3300),  \
    ("Jen", "Finance", 3900),    \
    ("Lucy", "Finance", 3900),   \
    ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000),\
    ("Saif", "Sales", 4100) \
  )

columns = ["emp_name","department","salary"]
emp_df = spark.createDataFrame(sampleData,columns)
# emp_df.show()
# 1. Row Number
# row_number() window function gives the sequential row number starting from 1 to the result of each partition.
#Way-1
# winSpec = Window.partitionBy("department").orderBy(desc("salary"))
# emp_df.withColumn("row_num",row_number().over(winSpec)).show()
#Way-2
# res = emp_df.select("emp_name","department","salary",functions.row_number().over(Window.partitionBy("department").orderBy(emp_df["salary"].desc())).alias("row_num"))
# res.show()
#way-3
# res = emp_df.select("*",functions.row_number().over(Window.partitionBy("department").orderBy(desc("salary"))).alias("row_num"))
# res.show()

x = ["Python",["Maths","Physics","Chemistry"]]

y = [(x[0], subject) for subject in x[1]]
print(y)
# print(x[0])