# -*- coding: utf-8 -*-
"""
TUPLES
"""

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])

dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])
