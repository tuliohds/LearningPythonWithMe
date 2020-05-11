#-*- coding: utf-8 -*-

# First Code, performing the classic Hello World
print("Hello World")

# Second Code is about mathematical expressions
# Addition
print("Addition: 10 + 2")
print(10 + 3)
# Subtraction
print("Subtraction: 32 - 2")
print(32 - 2)
# Multiplication
print("Multiplication: 10 x 10")
print(10 * 10)
# Division
print("Division: 10 / 2")
print(10 / 2)
# Rest of division
print("Rest of division: 10 / 3")
print(10 % 3)

# Now is time to use variables
# Variables on Python are sensitive case, and the atribution operator is '='  
msg = "Hello World using variables"
print(msg)

#Basic Data Types
# Intengral numbers - Example: 47
var1 = 1
print(var1)

# Float numbers - Example: 12.89
var2 = 1.2
print(var2)

# Text (String) - Example: Hello World
var3 = "I am a String"
print(var3)

# Boolean - Example: True or False
var4 = True
var5 = False
print(var4)
print(var5)

#Basic Operators
# Is used on operations in general
print("+ | Addition")
print("- | Subtraction")
print("* | Multiplication")
print("/ | Division")
print("** | Exponentiation")
print("% | Module")
print("= | Atribution Operation")

#Relationaly Operators
# Is used in comparison operations
print("== | Same")
print("!= | Different")
print("> | Larger")
print("< | Minor")
print(">= | Larger or Same")
print("<= | Division")

x = 2
y = 3

print(x > y) #False
print(y > x) #True
print(x == y) #False

#Logical Operators
print("AND | Two conditions must be True")
print("OR | At least one condition must be True")
print("NOT | Invert the value")

#Using the Logical operators
x = 3
y = 3
z = 3

print(x == y and x == y) #True
print(y != x and x == y) #False
print(y != x or x == y) #True

#Indentation
# For using conditional commands is important using indentation
# for using indentation is easy, need only press TAB on keyboard on code. 

#Conditional Commands
# if
x = 1
y = 1000

if x > y:
	print("x is greater than y")

if y > x:
	print("y is greater than x")

# if and else
x = 1000
y = 1

if y > x:
	print("y is greater than x")
else:
	print("x is greater than y")

# while
x = 0

while x < 5:
	print(x)
	x= x+1
	# x += 1 is same x= x+1

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

#Object
'''
It has been agreed that in Python everything is an object. In fact, Python is an object-oriented language.

Objects are instances of classes. For example, when you create a variable with a string, you are creating a string object.

Objects have attributes (characteristics) and methods (actions that can be applied).

Notice how to check attributes and methods to an object:

object.attribute
object.method( )

Translated with www.DeepL.com/Translator (free version)
'''