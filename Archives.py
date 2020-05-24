#-*- coding: utf-8 -*-

#Archives

# For opening a archive is necessary used the function Open, what have modes:
# Open function modes
#  r - only read
#  w - write (case the archive exist, he will wiped out and a new empty archive will be create)
#  a - read and write (add the new content in the end of archive)
#  r+ - read and write
#  w+ - write (the mode w+, like as the w, also erase the before content on the archive )
#  a+ - read and write (open the archive for actualization)

# Using fuction modes
w = open("archive1.txt", "w")

w.write("It is my new archive")

# Is important every close the archives
w.close()

# Functions for using when open archives 
#  read() - read all archive
#  readline() - read a line of archive
#  readlines() - read archive and stores in a list

# archive = open("archive.txt")

# print(archive) # <_io.TextIOWrapper name='archive.txt' mode='r' encoding='cp1252'> | incorrect result

#lines = archive.readlines()

#print(lines) # ['My archive\n', 'Hello world']

#for line in lines:
#	print(line) 

#text = archive.read()
#print(text)