# -*- coding: utf-8 -*-
"""
DICTIONARIES
"""

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print("carbon" in elements)
print(elements.get("dilithium"))

n = elements.get("dilithium")
print(n is None)
print(n is not None)

elements.get('kryptonite', 'There\'s no such element!')


"""
QUIZ- Definition
"""
# Define a Dictionary, population,
# that provides information
# on the world's largest cities.
# The key is the name of a city
# (a string), and the associated
# value is its population in
# millions of people.

#   Key     |   Value
# Shanghai  |   17.8
# Istanbul  |   13.3
# Karachi   |   13.0
# Mumbai    |   12.5

population = {"Shanghai":17.8, "Istanbul":13.3, "Karachi":13.0, "Mumbai":12.5}
print(population["Karachi"])
print(type(population))


"""
IDENTITIES
"""
a = [1, 2, 3]
b = a
c = [1, 2, 3]


print(a == b) #True
print(a is b) #True
print(a == c) #True
print(a is c) #False