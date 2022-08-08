#!/bin/sh
# bin/hadoop jar cc.jar CharCount io/input io/output1
# bin/hadoop jar crs.jar CountRS io/input io/output2
# bin/hadoop jar tw.jar TotalWords io/input io/output3
# bin/hadoop jar wc.jar WordCount io/input io/output4

rm -rf io/output1
rm -rf io/output2
rm -rf io/output3
rm -rf io/output4
{ /usr/bin/time hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -file mapper_CC.py -mapper mapper_CC.py -file reducer.py -reducer reducer.py -input io/input -output io/output1 ; } 2> tmp.txt

echo "Char Counter time: " > ts/time.txt
tail -n 1 tmp.txt >> ts/time.txt

# rm -rf io/output1
{ /usr/bin/time hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -file mapper_CRS.py -mapper mapper_CRS.py -file reducer.py -reducer reducer.py -input io/input -output io/output2 ; } 2> tmp.txt

echo "Counter RS time: " >> ts/time.txt
tail -n 1 tmp.txt >> ts/time.txt
 
# rm -rf io/output1
{ /usr/bin/time hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -file mapper_TW.py -mapper mapper_TW.py -file reducer.py -reducer reducer.py -input io/input -output io/output3 ; } 2> tmp.txt

echo "Total Words Counter time: " >> ts/time.txt
tail -n 1 tmp.txt >> ts/time.txt

# rm -rf io/output1
{ /usr/bin/time hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.3.3.jar -file mapper_WC.py -mapper mapper_WC.py -file reducer.py -reducer reducer.py -input io/input -output io/output4 ; } 2> tmp.txt

echo "Word Counter time: " >> ts/time.txt
tail -n 1 tmp.txt >> ts/time.txt

cat ts/time.txt