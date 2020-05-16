#-*- coding: utf-8 -*-

#Functions
# Functions are code block and only execute when calls
# In Python are using the word *def*

# Structure: def namefunction(parameter):
def sum(x,y):
	print(x+y)

sum(3,4) 

# but is more common use how below:
def sum(x,y):
	return x+y

def multiplicacion(x,y):
	return x*y

s = sum(2,3)
m = multiplicacion(2,3)

print(s)
print(m)

# other form for use
print(sum(s,m)) 