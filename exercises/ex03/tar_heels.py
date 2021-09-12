"""An exercise in remainders and boolean logic."""

__author__ = "730319407"


# Begin your solution here...

User_integer: int = 0
User_integer = User_integer + int(input("Enter an int:"))
i = User_integer 
s: str = ""

if i % 2 == 0 and i % 7 == 0:
    s = "TAR HEELS"
elif i % 2 == 0:
    s = "TAR"
elif i % 7 == 0:
    s = "HEELS"
else:
    s = "CAROLINA"

print(s)