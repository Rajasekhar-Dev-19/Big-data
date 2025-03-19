from pyspark.sql import SparkSession
from pyspark.sql.functions import col, isnull
import pyspark.sql.functions as f
from pyspark.sql.types import IntegerType

spark = SparkSession.builder.appName("Null Handling").getOrCreate()
file_path = "D:/Data/Department/dept_data_for_null_handling.txt"
# .option("nullValue", "null")
input_df = spark.read.format("csv").options(header=True,inferSchema=True).option("nullValue", "null").load(file_path)
# input_df.show(25)
# input_df.filter(~(isnull(col("dept_id")))).show()



# input_df.printSchema()
# null_df_0 = input_df.filter(col("dept_id") == 'NULL').filter((isnull(col("dept_id"))))
# # null_df_0.show()
# null_df = input_df.filter((isnull(col("dept_id")))).filter((isnull(col("dept_name")))).filter((isnull(col("dept_location")))) \
#             .filter(col("dept_id") == 'null') #.filter(col("dept_id") == '')
# # null_df.show(25)
# not_null_df = input_df.filter(~(isnull(col("dept_id")))).filter(~(isnull(col("dept_name")))).filter(~(isnull(col("dept_location")))) \
#             .filter(col("dept_id") != 'NULL').filter(col("dept_id") != '')
# not_null_df.show(25)

# input_df.distinct().orderBy("dept_id").show()
# input_df.dropDuplicates(["dept_id","dept_name"]).orderBy("dept_id").show()
# input_df.printSchema()
# input_df.fillna("NA").show()
# input_df.fillna("99999",["dept_id"]).fillna("NA",["dept_name"]).orderBy("dept_id").show(25)
# not_null_df.select("dept_id",not_null_df.dept_id.cast(IntegerType()))
# not_null_df.printSchema()

# input_df.distinct().show()
# input_df.dropDuplicates().sort("dept_id",ascending=False).show()
# input_df.dropDuplicates().orderBy(col("dept_id").asc()).show()
# input_df.dropDuplicates(["dept_id","dept_name"]).sort("dept_id").show()
# input_df.na.fill(0).na.fill("NA").show()
# input_df.fillna(0).fillna("NA").show() # 0 is replaced for all integer columns and NA is replaced with the all string columns
# input_df.fillna("NA",['dept_name']).fillna(0,['dept_id']).show() # 0 is only replaced on dept_id column and NA is only replaced on dept_name column

# input_df.dropna().show() # it will drop the entire rows when it will have all columns as null for records
# input_df.dropna(subset=['dept_id','dept_name','dept_location']).show() # it will drop the columns which will have the null values in it, here we can specify whatever columns we want

# (input_df.filter(~(isnull(col('dept_id'))))
#          .filter(~(isnull(col('dept_name'))))
#          .filter(~(isnull(col('dept_location')))).show())
# print(dir(f))