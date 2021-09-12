"""Repeating a beat in a loop."""

__author__ = "730319407"


# Begin your solution here...

User_string: str = input('What beat do you want to repeat?')
User_integer: int = 0
User_integer = User_integer + int(input("How many times do you want to repeat it?")) - 1
i: int = 0
result: str = User_string

while i < User_integer:
    result = result + " " + (User_string)
    i = i + 1
if User_integer <= 0:
    result = "No beat..."
    
print(result)
