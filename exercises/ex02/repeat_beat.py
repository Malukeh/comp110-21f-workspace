"""Repeating a beat in a loop."""

__author__ = "730319407"


# Begin your solution here...

User_string: str = input('What beat do you want to repeat?')
User_integer: int = int(input("How many times do you want to repeat it?"))

i: int = 0

while i < User_integer:
    print(User_string, end='')
    i = i + 1