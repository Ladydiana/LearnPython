# -*- coding: utf-8 -*-
"""
LIST COMPREHENSIONS
"""

#capitalized_cities = [city.title() for city in cities]
squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

#If you would like to add else, you have to move the conditionals to the beginning of the listcomp
squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)


"""
QUIZ - Extract First Names
"""
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names]
print(first_names)


"""
QUIZ - Multiples of Three
"""
count = 0
multiples_3 = [x * 3 for x in range(1, 21)]
print(multiples_3)


"""
QUIZ - Filter Names by Scores
"""
scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = passed = [name for name, score in scores.items() if score >= 65]
print(passed)