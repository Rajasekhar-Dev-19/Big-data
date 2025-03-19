from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, when
spark = SparkSession.builder.appName("Rename Columns").getOrCreate()

file_path = "F:/Bigdata/Datasets/india_states/states_1.csv"
file_path_1 = "F:/Bigdata/Datasets/persons_age/age.csv"

#Way-1
df = spark.read.option("header",True).csv(file_path)
#Way-2
df1 = spark.read.format("csv").load(file_path)
#Way-3
df2 = spark.read.option("header",True).csv(file_path)
df.printSchema()
# df.show(truncate=False)
# print("Before renaming the columns:",id(df)), ()

# ***************** select the columns ******************* #
# Way-1 (Specific columns)
df.select("state","capital") # not case sensitive
df.select(df.State,df.Capital) # case sensitive
df.select(df["STATE"],df["CAPITAL"]) # not case sensitive
print(df.columns) # it will bring the columns

# Way-2 (all columns )
# df.show()
# df.select("*").show()
# df.select([col for col in df.columns]).show()
# ***************** add the columns ******************* #
"""
using withColumn on a dataframe we can create a new column or override the columns names and change the data type of the column 
 
"""
df.withColumn("state",col("state")) # if we give the different column name it will create the another column
df.withColumn("state",col("state").cast("String")) # in this way we can cast the data type
# df.withColumn("state",(col("state")"-IND").show()
#***************** Renaming the columns ****************** #
# Way-1 (withColumnRenamed transformation)
"""
withColumnRenamed transformation we can rename the columns, here we have to pass two arguments
one is 'existing name' and another one is 'new name' 
Note: withColumnRenamed it will create the new dataframe, instead of modifying the dataframe. 
"""
renamed_df = df.withColumnRenamed("S.No.","serieal_num").withColumnRenamed("Largest city","largest_city")
# state_df = df.select("S.No.","State","Capital","Largest city","Statehood","Official languages","Vehicle code")
# print(df.count())
# renamed_df.show(truncate=False)
# print("After renaming the columns:",id(renamed_df))

# Way-2 (select transformation)
"""
with select transformation we can select the specific columns with col function and we can rename with the alias names as well.
if we have .(dots) in the columns names avoid those column names.
"""
# renemaed_df2 = df.select(col("State").alias("state_name"))
# state_df = df.select("*") # We can get the all records from dataframe
# state_df = df.selectExpr("State AS state_name","capital AS Capital_name", "Largest city AS largest_city"
#                          ,"Statehood","Official languages","Vehicle code")

state_df = df.selectExpr("state AS state_name","capital AS Capital_name","Statehood")
# state_df.show()

renamed_df2 = df.select(col("State"),col("Capital"),col("Largest city").alias("Largest_city")
                         ,col("Statehood"),col("Official languages").alias("official_languages"),col("Vehicle code").alias("Vehicle_code")
                         ,col("ISO"))

# renamed_df2.show(truncate=False)
new_df = renamed_df2.withColumn("Contry",lit("India").cast("String"))
# new_df.show()

student_data = [(111,"Asia",85.35),(222,"Africa",75.45),(333,"North America",65.74),(444,"South America",50.63),(555,"Antarctica",43.45),(666,"Europe",34.57),(777,"Australia",25.86)]

student_df = spark.createDataFrame(student_data,["id","student_name","percentage"])
stu_df = student_df.select(col("id"),col("student_name"),col("percentage").cast("Float"))
# stu_df.printSchema()
new_stu_df = stu_df.withColumn("grade", when(col("percentage") >= 75, "A Grade")
                                                    .when(col("percentage") >= 60, "B Grade")
                                                    .when(col("percentage") >= 50, "C Grade")
                                                    .when(col("percentage") >= 30, "D Grade")
                                                    .otherwise("Fail"))
# new_stu_df.show()