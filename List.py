#-*- coding: utf-8 -*-

#List

# Represent data sets, with:
#  Numbers: [1,2,3,4,5]
#  Strings: ["ball","shoes","rain"]

list_fruit = ["apple","watermelon","avocate"]
print(list_fruit)
print(list_fruit[0]) #apple
print(list_fruit[1]) #watermelon
print(list_fruit[2]) #avocate
# print(list_fruit[4]) #error

list_numbers = [1,2,3,4,5]
print(list_numbers)

list_mix = [1, "teste" , False , 9.09]
print(list_mix)

# other form for use list
for item in list_fruit:
	print(item)

# count the number of content in list
count = len(list_fruit)
print(count) # 3

# adding content in list
list_fruit.append("limon")
print(list_fruit)

# searching content on list
if 7 in list_numbers:
	print("Exist in list number")
else:
	print("Not exist in list number")

# removing content on list
del list_fruit[2:]  # removing value using position
print(list_fruit) # ['apple', 'watermelon']

# delete all list
del list_fruit[:]
print(list_fruit) # []

# Now is time to order lists
new_list_numbers1 = [124,123,2,3,4,6,3,1,567,345]
new_list_numbers2 = [232,34,45,61,3,1,567,345]
print(new_list_numbers1) 
print(new_list_numbers2) 

# For order a list and variables, exist two forms:
new_list_numbers1.reverse()
print(new_list_numbers1)
new_list_numbers1.sort()
print(new_list_numbers1) # [1, 2, 3, 3, 4, 6, 123, 124, 345, 567]
new_list_numbers1.sort(reverse=True)
print(new_list_numbers1)

new_list_numbers2 = sorted(new_list_numbers2)
print(new_list_numbers2) # [1, 3, 34, 45, 61, 124, 232, 345, 567]

