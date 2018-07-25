# -*- coding: utf-8 -*-
"""
ZIP & ENUMERATE
"""

list(zip(['a', 'b', 'c'], [1, 2, 3])) # output [('a', 1), ('b', 2), ('c', 3)]

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list) #unzip using asterisk

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)
    
"""
QUIZ - Zip Coordinates
"""
# Use zip to write a for loop that creates a string specifying the label and 
# coordinates of each point and appends it to the list points. 
# Each string should be formatted as label: x, y, z. 
# For example, the string for the first coordinate should be F: 23, 677, 4.
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

points = []
# write your for loop here
for point in zip(labels, x_coord, y_coord, z_coord):
    points.append("{}: {}, {}, {}".format(*point))
#points = list(zip(labels, x_coord, y_coord, z_coord))

for point in points:
    print(point)
    
    
"""
QUIZ - Zip Lists to a Dictionary
"""
cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

cast = dict(zip(cast_names, cast_heights))# replace with your code
print(cast)


"""
QUIZ - Unzip Tuples
"""
cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

names, heights = zip(*cast)
print(names)
print(heights)


"""
QUIZ - Transpose with Zip
"""
data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

data_transpose = tuple(zip(*data))# replace with your code
print(data_transpose)


"""
QUIZ - Enumerate
"""
cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# write your for loop here
for i, character in enumerate(cast):
    cast[i] = character + " " + str(heights[i])

print(cast)