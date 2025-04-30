import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
sc = spark.sparkContext
sc.setLogLevel("OFF")
wordsList = ['python', 'java', 'ottawa', 'ottawa', 'java', 'news']
wordsRDD = sc.parallelize(wordsList,4)
print(wordsRDD.collect())
wordPairs = wordsRDD.map(lambda w: (w, 1))
print (wordPairs.collect())
wordCountsCollected = wordPairs.reduceByKey(lambda x, y: x+y)
print(wordCountsCollected.collect())
