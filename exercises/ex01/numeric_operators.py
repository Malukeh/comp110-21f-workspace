"""Demonstrating how these four numerical operators work."""

__author__ = "730319407"

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))

print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(left_hand_side ** right_hand_side))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(left_hand_side / right_hand_side))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(left_hand_side // right_hand_side))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(left_hand_side % right_hand_side))