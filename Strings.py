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

#In Python, Strings are objects and you can apply methods to them
# Using the method for tinier the words on phrase

a = "CaLiFoRNia"
b = "DReaM"

concat = a + " and " + b
print(concat) # All letters are how initially 	
print(concat.lower()) # All letters are tiny
print(concat.upper()) # All letters are capital	

# Other form
concat = concat.lower() # All letters are tiny, but now is using variable
print(concat)

# For create a line break
concat = "\n" + a + "\n and \n" + b 
print(concat) 

# For removing special characters and space on the begin and in the end.
print(concat.strip()) 

# Make string in array and using split
my_string = "2B or not 2B"

my_list = my_string.split(" ")
print(my_list)

# Now removing one letter
my_list = my_string.split("B")
print(my_list)

# Searching substrings
search = my_string.find("not")
print(search) # is return the position on the array
print(my_string[search:]) # return after in the mark on variable  

#if search a word what not exist in the context?
search = my_string.find("nothing")
print(search) # is returned -1 position on the array

# and finally, one interesting method is replace
search = my_string.replace("2B","to be")
print(search) # to be or not to be