# -*- coding: utf-8 -*-
"""
STRINGS
"""


"""
QUIZ - strings
"""
username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."
print(username + ' accessed the site ' + url + ' at ' + timestamp + '.')


"""
QUIZ - len
"""
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

#todo: calculate how long this name is
name_length = len(given_name + middle_names + family_name)+2

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)


"""
QUIZ - conversions
"""
mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.
string_format = "This week's total sales: "
total_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
print(string_format + str(total_sales))              


"""
QUIZ - format
"""
# Write two lines of code below, each assigning a value to a variable
favorite_book = "Harry Potter"
second_favorite = "The Count of Monte Cristo"

# Now write a print statement using .format() to print out a sentence and the 
#   values of both of the variables
print("My favorite books are {} and {}.".format(favorite_book, second_favorite))