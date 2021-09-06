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


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Fortune cookie."""
    x = randint(1, 100)
    if x <= 25:
        return "Your life will be peaceful."
    else:
        if x <= 50:
            return "A beautiful, smart, and loving person will be coming into your life."
        else:
            if x <= 75:
                return "Your life will be beautiful." 
                
            else:
                return "Soon life will become more interesting."


if __name__ == "__main__":
    main()