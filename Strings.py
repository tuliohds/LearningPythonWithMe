#-*- coding: utf-8 -*-

#Strings

# String is a type of data in which collections of characters (text) are stored. 
# String using "".

a = "Santiago"
b = "Blue"

# Concatenating strings
concat = a + " and " + b
print(concat)

# Counting letters on string
count = len(concat)
print(count)

# Sailing in the index
print(b[0]) #B
print(b[1]) #l
print(b[2]) #u
print(b[3]) #e

# Show string in parts
print(concat[0:8]) #Santiago
print(concat[13:17]) #Blue
print(concat[0:17]) #Santiago and Blue