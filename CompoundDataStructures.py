# -*- coding: utf-8 -*-
"""
COMPOUND DATA STRUCTURES
"""

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}

helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight

oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)



# todo: Add an 'is_noble_gas' entry to the hydrogen and helium dictionaries
# hint: helium is a noble gas, hydrogen isn't
hydrogen = {"number": 1,
            "weight": 1.00794,
            "symbol": "H",
            "is_noble_gas": False
            }
helium = {"number": 2,
          "weight": 4.002602,
          "symbol": "He",
          "is_noble_gas": True
          }
elements["hydrogen"] = hydrogen
elements["helium"] = helium

print(elements)

#or
#elements['hydrogen']['is_noble_gas'] = False
#elements['helium']['is_noble_gas'] = True
