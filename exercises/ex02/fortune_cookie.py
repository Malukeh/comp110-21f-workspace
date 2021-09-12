"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730319407"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...


print("Your fortune cookie says...")


Fortune_1: str = "You will meet a good friend."
Fortune_2: str = "The best year of your life is about to approach you."
Fortune_3: str = "You will give hapiness to a loved one."
Fortune_4: str = "You will learn to love yourself."


x: int = randint(1, 100)
if x <= 25:
    print(Fortune_1)
else:
    if x <= 50:
        print(Fortune_2)
    if x <= 75:
        print(Fortune_3)  
    else:
        print(Fortune_4)


print("Now, go spread positive vibes!")