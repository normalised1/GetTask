import datetime
from task import GetTask

date = datetime.datetime.now()
print GetTask(date.microsecond)
