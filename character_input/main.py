from datetime import date

# MVP: Print the year when the user will turn 100 years old.

def year_of_100(user_name, user_age):
    current_year = date.today().year

    difference_to_100 = 100 - user_age
    year_of_100 = current_year + difference_to_100

    return f'{user_name} will turn 100 years old in {year_of_100}'

# Input
user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))

if user_name == ' ' or user_name == '' or user_name == False:
    print('Invalid input. Please enter a valid name.')
else:
    print(year_of_100(user_name, user_age))

# Addon: Ask the user if they want to make a copy of the message. If they do, ask them how many copies they want to make. Then print the message that many times.
ask_for_copy = input('Do you want to make a copy of the message? (y/n): ')

if ask_for_copy == 'y':
    copy_number = int(input('Enter the number of copies you want to make: '))
    message = year_of_100(user_name, user_age)
    counter = 0

    while counter < copy_number:
        if counter != copy_number - 1:
            print(message + '\n')
        else:
            print(message)
        counter += 1
        
else:
    print('See ya later!')

