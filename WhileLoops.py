# -*- coding: utf-8 -*-
"""
WHILE Loop
"""

# Example
card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
    

# Print out a word's letters, one per line. 
print_str = "Water falls"
i = 0
while i < len(print_str):
    print(print_str[i])
    i += 1
    
    
#Find the Factorial of a Number, using While Loop.
i = 1
number = 5
factorial = 1

while i<=number:
    factorial*=i
    i+=1
    
print(factorial)


"""
QUIZ - Count By
"""
start_num = 1 #provide some start number
end_num = 10 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by 
break_num = start_num

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
while break_num<end_num:
    print(break_num)
    break_num += count_by


"""
QUIZ - Nearest Square
"""
limit = 40
i = 1

while (i*i)<limit:
    i+=1
    
nearest_square=(i-1)*(i-1)
print(nearest_square)
