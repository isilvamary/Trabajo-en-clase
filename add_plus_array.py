import random

list=[]
sum=0

for i in range(0,10):
    list.append(random.random())

for x in list:
    sum += x

print(sum)
