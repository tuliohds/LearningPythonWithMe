#-*- coding: utf-8 -*-

# For finish the lessons, go making with me one list of exercises

# 1 - Make a program that receive the age of a user and tell if him is a adult

def isadult(age):
	if age < 18:
		print("Isn't adult")
	else:
		print("Is adult")
	

isadult(11)
isadult(18)

# 2 - Make a program that receive two grades for the user. If grade is bigger or same six, write aproved, 
# else write reproved.

def isaproved(note1,note2):
	media = (note1+note2) / 2;
	if media > 5:
		print("Aproved")
	else:
		print("Reproved")
	
isaproved(3,8)
isaproved(1,7)

# 3 - Write a program what order a numeric list with three elements.

def numericlist(num1,num2,num3):
	nlist = [num1,num2,num3]
	nlistorder = sorted(nlist)
	print(nlist)
	print(nlistorder)
	
numericlist(3,8,4)
numericlist(1,7,2)

# 4 - Write a program what receive two number and a operator, and make the mathematical operation. 

def mathematicaloperatin(num1,num2,operator):
	if operator == '+':
		print(num1 + num2)
	elif operator == '-':
		print(num1 - num2)
	elif operator == '/':
		print(num1 / num2)
	elif operator == '*':
		print(num1 * num2)
	else:
		print('Please insert a valid operator.')
	
mathematicaloperatin(9,8,'-')
mathematicaloperatin(2,5,'*')
mathematicaloperatin(2,2,'%')