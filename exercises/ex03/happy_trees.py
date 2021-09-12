"""Drawing forests in a loop."""

__author__ = "730319407"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

User_input: int = int(input('Depth:'))

i = 1

while i <= User_input:
    x: int = 1
    string: str = ""
    while x <= i:
        string += TREE
        x += 1
    print(string)
    i += 1