# -*- coding: utf-8 -*-
"""
GENERATORS
"""

sq_list = [x**2 for x in range(10)]  # this produces a list of squares

sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares

def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

for x in my_range(5):
    print(x)


"""
QUIZ - Implement my_enumerate
"""
lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    # Implement your generator function here
    for element in iterable:
        yield count, element
        count += 1


for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))
    

"""
QUIZ - Chunker
"""
def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]
        
for chunk in chunker(range(25), 4):
    print(list(chunk))