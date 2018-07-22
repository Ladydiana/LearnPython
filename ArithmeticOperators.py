# -*- coding: utf-8 -*-
"""
ARITHMETIC OPERATORS
"""

# QUIZ - Average
""" 
Write an expression that calculates the average of 23, 32 and 64.
Place the expression in a print statement.
"""
print((23+32+64)/3)

#or use the statistics library
#more useful for when there is an unlimited number of numbers
import statistics
print(statistics.mean([23, 32, 64]))


# QUIZ-Calculate
"""
Two parts of a floor need tiling. 
One part is 9 tiles wide by 7 tiles long, the other is 5 tiles wide by 7 
tiles long. Tiles come in packages of 6.
How many tiles are needed?
"""
print(9*7+5*7)
"""
You buy 17 packages of tiles containing 6 tiles each. 
How many tiles will be left over?
"""
print(17*6-(9*7+5*7))


