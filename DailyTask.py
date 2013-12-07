import datetime
from task import GetTask

date = datetime.datetime.now()
day = date.day + 102 
month = date.month
year = date.year
seed = day * 100 + month * 1000 + year
print GetTask(seed)


