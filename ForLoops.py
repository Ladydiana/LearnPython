# -*- coding: utf-8 -*-
"""
FOR LOOPS
"""

cities = ['new york city', 'mountain view', 'chicago', 'los angeles']
for city in cities:
    print(city)
    
for i in range(3):
    print("Hello!")

for index in range(len(cities)):
    cities[index] = cities[index].title()
    
#Iterating through dictionaries
cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))
    

"""
QUIZ - make usernames
"""    
names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for i in range(len(names)):
    usernames.append(names[i].replace(' ', '_').lower())

print(usernames)

"""
QUIZ - make usernames directly without using a variable
"""
usernames = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]

# write your for loop here
for i in range(len(usernames)):
    usernames[i] = usernames[i].replace(' ', '_').lower()

print(usernames)


"""
QUIZ - check if XML
"""
#Write a for loop that iterates over a list of strings, tokens, and counts how many of them are XML tags.
tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here
for i in range(len(tokens)):
    if tokens[i].startswith('<') and tokens[i].endswith('>'):
        count+=1

print(count)


"""
QUIZ - make HTML
"""
#Write some code, including a for loop, that iterates over a list of strings and creates a single string, html_str, which is an HTML list.

items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here

for i in range(len(items)):
    html_str += "<li>"
    html_str += items[i]
    html_str += "</li>\n"
html_str += "</ul>\n"
print(html_str)


"""
QUIZ - iterating through dictionaries
"""
# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        result += value

print(result)


# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
#if the key is in the list of fruits, add to fruit_count.
#if the key is not in the list, then add to the not_fruit_count
for key, value in basket_items.items():
    #if the key is in the list of fruits, add the value (number of fruits) to result
    if key in fruits:
        fruit_count += value
    else:
        not_fruit_count += value
