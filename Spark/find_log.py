from os import listdir
from os.path import isfile, join
import sys

mypath = '/opt/spark/logs'

onlyfiles = [
    f for f in listdir(mypath) if isfile(join(mypath, f))
]

for file_name in onlyfiles:
    if file_name.startswith('spark--org.apache.spark.deploy.master'):
        sys.stdout.write(mypath + "/" + file_name)