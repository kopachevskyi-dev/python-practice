from datetime import date

current_year = date.today().year

user_name = input('Enter your name: ')
user_age = int(input('Enter your age: '))

if user_name == ' ' or user_name == '' or user_name == False:
    print('Invalid input. Please enter a valid name.')
else:
    difference_to_100 = 100 - user_age
    year_of_100 = current_year + difference_to_100

    print(f'{user_name} will turn 100 years old in {year_of_100}')