"""
Lottery numbers

In this problem, we've provided you with a set of lottery numbers:

lottery_numbers = {13, 21, 22, 5, 8}
You must define a list of two players, each with a name and another set of numbers.

Players in your list should be dictionaries following this format:

{
    'name': 'PLAYER_NAME',
    'numbers': {1, 2, 3, 4, 5}
}

You can come up with each player name and numbers!

Printing out their luck

Then for each player, print out a nice string that contains their name and how many numbers they got right (as we've done before, you can intersect their numbers with the lottery_numbers  variable provided). 
You'll then need to calculate the length of the resulting set to get how many numbers they got right.

This string doesn't have to have a particular format, it just must include both the name and how many numbers they got right.

Happy coding!
"""

lottery_numbers = {13, 21, 22, 5, 8}

# Define a list with two players
players = [
    {
        "name": "PLAYER_A",
        "numbers": {5, 76, 34, 22, 12}
    },
    {
        "name": "PLAYER_B",
        "numbers": {22, 8, 14, 9, 3}
    }
]

# Calculate the length of the resulting set to get how many numbers they got right
player_a_numbers = players[0]['numbers'].intersection(lottery_numbers)
player_b_numbers = players[1]['numbers'].intersection(lottery_numbers)

# Count the numbers they got right
player_a_numbers_count = len(player_a_numbers)
player_b_numbers_count = len(player_b_numbers)

# Print out the result
print(f"{players[0]['name']} got: {player_a_numbers_count} numbers right! Thouse numbers are: {player_a_numbers}")
print(f"{players[1]['name']} got: {player_b_numbers_count} numbers right! Thouse numbers are: {player_b_numbers}")