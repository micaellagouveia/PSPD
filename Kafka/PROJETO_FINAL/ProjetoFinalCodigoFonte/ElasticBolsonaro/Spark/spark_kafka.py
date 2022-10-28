from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import window
from pyspark.sql.functions import split


spark = SparkSession \
    .builder \
    .appName("SparkKafkaWordCount") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")

# Subscribe to 1 topic
df = spark \
  .readStream \
  .format("kafka") \
  .option("kafka.bootstrap.servers", "localhost:9092") \
  .option("subscribe", "bolsonaro_treated_messages") \
  .option("failOnDataLoss", "false") \
  .load()

# Split the lines into words
words = df.select(
   explode(
       split(df.value, " ")
   ).alias("value")
)

# Generate running word count
words = words.groupBy("value").count()
wordCounts = words.withColumnRenamed('count', 'key')

# Start running the query that prints the running counts to the console
# query = wordCounts \
#     .writeStream \
#     .format("console") \
#     .start() \
#     .awaitTermination()

finalStream = wordCounts.selectExpr("CAST(key AS STRING)","CAST(value AS STRING)").writeStream \
    .outputMode("update") \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("checkpointLocation", "/tmp") \
    .option("failOnDataLoss", "false") \
    .option("topic", "all_words_bolsonaro") \
    .start() \
    .awaitTermination()
