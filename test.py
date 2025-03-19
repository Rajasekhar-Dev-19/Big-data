from pyspark.sql import SparkSession  # We have to import
from pyspark.sql import Window, functions
from pyspark.sql.functions import row_number, desc

spark = SparkSession.builder.appName('Window Functions').getOrCreate()

sampleData = (("James", "Sales", 3000), \
              ("Michael", "Sales", 4600), \
              ("Robert", "Sales", 4100), \
              ("Maria", "Finance", 3000), \
              ("James", "Sales", 3000), \
              ("Scott", "Finance", 3300), \
              ("Jen", "Finance", 3900), \
              ("Lucy", "Finance", 3900),    \
              ("Jeff", "Marketing", 3000), \
    ("Kumar", "Marketing", 2000), \
    ("Saif", "Sales", 4100) \
    )

columns = ["emp_name", "department", "salary"]
emp_df = spark.createDataFrame(sampleData, columns)
emp_df.show()