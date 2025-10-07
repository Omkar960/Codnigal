import random
import time

def my_func(Start_date,End_date):

 print("A date between",Start_date, "and" ,End_date, "will be generated")
 randomGenerator = random.random()
 dateFormat = '%d/%m/%Y'
 startTime = time.mktime(time.strptime(Start_date,dateFormat))
 endTime = time.mktime(time.strptime(End_date,dateFormat))
 randomtime = startTime + randomGenerator * (endTime - startTime)
 randomdate = time.strftime(dateFormat, time.localtime(randomtime))
 return randomdate



print(my_func("1/11/2016","3/7/2022"))

