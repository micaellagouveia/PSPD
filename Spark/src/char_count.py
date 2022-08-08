import time

start_time = time.time()
 
from pyspark import SparkContext
 
if __name__ == "__main__":
	
	# create Spark context with necessary configuration
	sc = SparkContext("local","PySpark Word Count Exmaple")
	
	# read data from text file and split each line into words
	words = sc.textFile("io/text.txt").flatMap(lambda line: line.split(" "))
	
	def count_chars(word):
		if len(word) == 6:
			return ("6", 1)
		elif len(word) == 8:
			return ("8", 1)
		elif len(word) == 11:
			return ("11", 1)
		else:
			return ("", 0)

	
	# count the occurrence of each word with 6 and 8 chars
	charCounts = words.map(lambda word: count_chars(word)).reduceByKey(lambda a,b:a +b)
	
	# save the counts to output
	charCounts.saveAsTextFile("io/output1/")

with open('io/output1/part-00000', 'a') as file:
	print(f" {(time.time() - start_time)} seconds", file=file)
