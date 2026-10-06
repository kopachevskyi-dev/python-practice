"""
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = input('Provide a string: ').lower()

# First simpler solution
"""
if user_input.lower() == user_input[::-1].lower():
    print(f"'{user_input}' is a palindrome string!")
else:
    print("Provided string is not a palindrome.")
"""

# Second solution

reversed_list = []

for reversed_index in range(len(user_input) - 1, -1, -1):
    reversed_list.append(user_input[reversed_index])

reversed_string = "".join(reversed_list)

if reversed_string == user_input:
    print(f"'{user_input}' is a palindrome string!")
else:
    print("Provided string is not a palindrome.")