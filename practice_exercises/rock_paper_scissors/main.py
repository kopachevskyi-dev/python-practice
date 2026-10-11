"""
Make a two-player Rock-Paper-Scissors game. 
(Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
- Rock beats  scissors
- Scissors beats  paper
- Paper beats rock
"""

rules = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

options = ['rock', 'scissors', 'paper']

print("""
Welcome to the Rock-Paper-Scissors Game!

Moves: rock, scissors, paper
- Enter 'p' to play
- Enter 'q' to exit
""")

while True:
    user_input = input('\nYour choice (p/q): ').strip().lower()

    if user_input == 'p':
        player_1_input = input('[PLAYER 1] rock / scissors / paper: ').strip().lower()
        player_2_input = input('[PLAYER 2] rock / scissors / paper: ').strip().lower()

        if player_1_input not in options or player_2_input not in options:
            print('Incorrect data. Use: rock, scissors, or paper.')
        elif player_1_input == player_2_input:
            print('DRAW!')
        elif rules[player_1_input] == player_2_input:
            print('Congratulations! PLAYER 1 WON!')
        elif rules[player_2_input] == player_1_input:
            print('Congratulations! PLAYER 2 WON!')
    elif user_input == 'q':
        print('Thanks for playing.')
        break
    else:
        print("Incorrect input. Enter 'p' to play or 'q' to exit.")