"""
Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don't know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

user_input = int(input('Provide a number: '))
divisors = []

for divisor in range(1, user_input + 1):
    if user_input % divisor == 0:
        divisors.append(divisor)

print(f"Divisors are: {divisors}")