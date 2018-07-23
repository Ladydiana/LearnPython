# -*- coding: utf-8 -*-
"""
CONDITIONAL STATEMENTS
"""

"""
General Formatting
"""
season="summer"

if season == 'spring':
    print('plant the garden!')
elif season == 'summer':
    print('water the garden!')
elif season == 'fall':
    print('harvest the garden!')
elif season == 'winter':
    print('stay indoors!')
else:
    print('unrecognized season')


"""
QUIZ - points
"""
points = 174  # use this input to make your submission
#prize = None
# write your if statement here

if(1<points and points<=50):
    prize="wooden rabbit"
elif(50<points and points<=150):
    prize="no prize"
elif(150<points and points<=180):
    prize="wafer-thin mint"
elif(180<points and points<=200):
    prize="penguin"
else:
    prize=None
    
if(prize!=None and prize!='no prize'):
    print("Congratulations! You won a {}!".format(prize))
else:
    print("Oh dear, no prize this time.")
    
    
"""
QUIZ - guess game
"""
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
answer = 37 #provide answer
guess = 10 #provide guess

if guess<answer:
    result = "Oops!  Your guess was too low."
elif guess>answer:
    result = "Oops!  Your guess was too high."
elif guess==answer: #provide conditional
    result = "Nice!  Your guess matched the answer!"

print(result)


"""
QUIZ - taxes
"""
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right
# amount.
# '''
state = 'MN'#Either CA, MN, or NY
purchase_amount = 120 #amount of purchase

if state=='CA': #provide conditional for checking state is CA
    tax_amount = .075
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=='MN':#provide conditional for checking state is MN
    tax_amount = .095
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

elif state=='NY':#provide conditional for checking state is NY
    tax_amount = .089
    total_cost = purchase_amount*(1+tax_amount)
    result = "Since you're from {}, your total cost is {}.".format(state, total_cost)

print(result)