# -*- coding: utf-8 -*-
"""
VARIABLES
1. Only use ordinary letters, numbers and underscores in your variable names. 
   They can’t have spaces, and need to start with a letter or underscore.
2. You can’t use reserved words or built-in identifiers that have important 
purposes in Python.
3. The pythonic way to name variables is to use all lowercase letters and 
underscores to separate words.
"""

# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall -= rainfall*0.1

# add the rainfall variable to the reservoir_volume variable
reservoir_volume += rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume += reservoir_volume * 0.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume -= reservoir_volume * 0.05

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.5e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)