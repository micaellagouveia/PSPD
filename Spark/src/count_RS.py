import time

start_time = time.time()
 
from pyspark import SparkContext
 
if __name__ == "__main__":
	
	# create Spark context with necessary configuration
	sc = SparkContext("local","PySpark Word Count Exmaple")
	
	# read data from text file and split each line into words
	words = sc.textFile("io/text.txt").flatMap(lambda line: line.split(" "))
	
	def count_RS(word):
		if word.startswith("R"):
			return ("R", 1)
		elif word.startswith("S"):
			return ("S", 1)
		else:
			return ("", 0)

	
	# count the occurrence of each word beginning with R and S
	rsCounts = words.map(lambda word: count_RS(word)).reduceByKey(lambda a,b:a +b)
	
	# save the counts to output
	rsCounts.saveAsTextFile("io/output2/")

with open('io/output2/part-00000', 'a') as file:
	print(f" {(time.time() - start_time)} seconds", file=file)