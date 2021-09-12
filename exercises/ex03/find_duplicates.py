"""Finding duplicate letters in a word."""

__author__ = "730319407"

User_string: str = input('Enter a word:')
count: int = 0

i: int = 0
result: bool = False

while i < len(User_string):
    x = i + 1
    while x < len(User_string):
        if User_string[i] == User_string[x]:
            result = True
        x += 1
    i += 1

print(result)