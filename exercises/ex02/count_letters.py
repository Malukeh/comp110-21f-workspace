"""Counting letters in a string."""

__author__ = "730319407"


# Begin your solution here...

x: str = input('What letter do you want to seach for?:')
User_string: str = input('Enter a word:')
count: int = 0

i: int = 0

while i < len(User_string):
    if x == User_string[i]:
        count = count + 1
    i = i + 1

print("Count:" + str(count))
