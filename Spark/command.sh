#!/bin/sh
spark-submit src/char_count.py
echo "Char Counter time: " > ts/time.txt
tail -n 1 io/output1/part-00000 >> ts/time.txt

spark-submit src/count_RS.py
echo "Counter RS time: " >> ts/time.txt
tail -n 1 io/output2/part-00000 >> ts/time.txt

spark-submit src/total_words.py
echo "Total Words Counter time: " >> ts/time.txt
tail -n 1 io/output3/part-00000 >> ts/time.txt

spark-submit src/word_count.py
echo "Word Counter time: " >> ts/time.txt
tail -n 1 io/output4/part-00000 >> ts/time.txt


# python find_log.py | xargs -0 tail -f
cat ts/time.txt