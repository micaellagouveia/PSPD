import time

start_time = time.time()
 
from pyspark import SparkContext
 
if __name__ == "__main__":
	
	# create Spark context with necessary configuration
	sc = SparkContext("local","PySpark Word Count Exmaple")
	
	# read data from text file and split each line into words
	words = sc.textFile("io/text.txt").flatMap(lambda line: line.split(" "))
	
	# count the occurrence of each word
	wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
	
	# save the counts to output
	wordCounts.saveAsTextFile("io/output4/")

with open('io/output4/part-00000', 'a') as file:
	print(f" {(time.time() - start_time)} seconds", file=file)