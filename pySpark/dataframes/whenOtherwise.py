from pyspark.sql import SparkSession
from pyspark.sql.functions import col, round, when

spark = SparkSession.builder.appName("When Otherwise").getOrCreate()

file_path="F:\Bigdata\Datasets\student.txt"
student_df = spark.read.csv(file_path,header=True,inferSchema=True)
df = student_df.withColumn("Total",(student_df.maths+student_df.physics+student_df.chemistry))\
.withColumn("percentage",round((col("Total")/300)*100,2))

result_df = df.withColumn("Grade",when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=90) ,"A+")\
                          .when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=80) ,"A")\
                          .when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=70) ,"B+")\
                          .when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=60) ,"B")\
                          .when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=50) ,"C+")\
                          .when((col("maths")>=35) & (col("physics") >=35) & (col("chemistry")>=35) & (col("percentage")>=35) ,"C")\
                          .otherwise("Fail")
                          )
result_df.show()