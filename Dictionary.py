#-*- coding: utf-8 -*-

#Dictionary

# Dictionery are associations lists compose with:
#	- a key
# 	- a correspondent value

my_dictionary = {"A":"Academic","B":"Ball","C":"Car"}

print(my_dictionary["A"]) # Academic
print(my_dictionary) # {'A': 'Academic', 'B': 'Ball', 'C': 'Car'}

for key in my_dictionary:
	print(f"{key}: {my_dictionary[key]})

for i in my_dictionary.items():
	print(i)

for t in my_dictionary.values():
	print(t)

for v in my_dictionary.keys():
	print(v)
