#-*- coding: utf-8 -*-

#Repetitive Links
# For using list with values
list1 = [1,2,3,4,5]
list2 = ["Hello","World","!"]
list3 = [0,"Hello","Salad","Oil",9.99,True]

for i in list3:
	print(i)

#Now is a For using range
## If you use a number, the number will be counted.
for i in range(10):
	print(i)

## If you use two the first number will be the beginning and the second the limit.
for i in range(10,20):
	print(i)

## If you use three the number will be divided.
for i in range(10,20,2):
	print(i)