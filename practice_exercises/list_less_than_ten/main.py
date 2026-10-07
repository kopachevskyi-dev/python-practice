"""
Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:
1. Instead of  printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list. Write this in one line of Python.
2. Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
"""

# Initial data
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# MVP
for num in a:
    if num < 5:
        print(f"{num} is less than 5.")

# First extra
print(f"{[num for num in a if num < 5]}")

# Second extra
user_input = int(input('Provide a number: '))

print(f"List of numbers that are smaller: {[num for num in a if num < user_input ]}")