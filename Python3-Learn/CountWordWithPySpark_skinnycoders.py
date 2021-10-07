# // AUTHOR: Ristanto Rizki
# // Python3 Concept: Count a word in file with pySpark
# // GITHUB: https://github.com/SkinnyCoders

from pyspark.sql import SparkSession

# your file 
logfile = "/home/baskara/Downloads/cerpen.txt"
spark = SparkSession.builder.appName("simpel spark").getOrCreate()
logData = spark.read.text(logfile).cache()

numAs = logData.filter(logData.value.contains('a')).count()

print(numAs)
