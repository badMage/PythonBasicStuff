#!/usr/bin/env python3

# import modules used here -- sys is a very standard one
# common standard library modules: System (sys), Operating System/File System etc. (os), Regular Expressions (re)
import sys
import os
import re

# in this case we only import the argv attribute (list of system arguments) from the "sys" module
# now we can refer to argv only by typing the short name (just argv instead of sys.argv)
from sys import argv

# defining a new function called "hello"
def hello():
	print("hello")

# gather our code in a main() function
def main():
	# in this case sys.argv[0] is the first argument after calling the python program/interpreter 
	print("HelloThere", sys.argv[0]) # expected output: "HelloThere main.py"
	hello()
	
	if len(sys.argv) > 1:
		print("HelloThere", sys.argv[0], sys.argv[1]) # expected output: "HelloThere main.py John" when executing: python main.py John
	# in general sys.argv is the list of command line arguments

	# we define a string variable called "var" which contains a string value "John"
	var = "John"
	var += str(324) # in this case we append 324 to the "var" variable (now var contains "John324")
	print(var)

	# turning the value of the "var" variable to lowercase
	# the "var" variable returns the lowercase string of a given/existing string (now "var" contains the value "john324")
	var = var.lower() 
	print(var)

	# writing an empty for loop
	for i in range(0, 10, 2):
		pass
	
	condition = True

	# writing an empty while loop
	while condition:
		condition = False

	print("end of program")



# standard boilerplate to call the main() function to begin the program
# in this case a standard variable called "__name__" is being set to "__main__"
if __name__ == "__main__":
	main()
