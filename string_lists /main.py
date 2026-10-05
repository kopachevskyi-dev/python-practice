"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input('Provide a string: ')

if user_input.lower() == user_input[::-1].lower():
    print(f"'{user_input}' is a palindrome string!")
else:
    print("Provided string is not a palindrome.")