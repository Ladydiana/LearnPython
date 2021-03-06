# -*- coding: utf-8 -*-
"""
Standard Library
"""
import math

print(math.exp(3))


"""
Write a function called generate_password that selects three random words from the list of words word_list and concatenates them into a single string. 
Your function should not accept any arguments and should reference the global variable word_list to build the password.
"""
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
# It should return a string consisting of three random words 
# concatenated together without spaces
def generate_password():
    generated_string= ""
    for i in range(3):
        generated_string += word_list[random.randint(0, len(word_list)-1)]
    return generated_string

# test your function
print(generate_password())