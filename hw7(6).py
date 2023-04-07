# Напишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументівНапишіть функцію, яка приймає два аргументи.
# Якщо обидва аргумени відносяться до числових типів функція пермножує ці аргументи і повертає результат
# Якшо обидва аргументи відносяться до типу стрінг функція обʼєднує їх в один і повертає
# В будь-якому іншому випадку - функція повертає кортеж з двох агрументів

def two_args_func(arg_1, arg_2):
    if isinstance(arg_1, (int, float)) and isinstance(arg_2, (int, float)):
        return arg_1 *arg_2
    elif isinstance(arg_1, str) and isinstance(arg_2, str):
        return arg_1 + arg_2
    return arg_1, arg_2

print(two_args_func(7, 12.5))
print(two_args_func('a', None))
print(two_args_func('a', 'b'))

# Візьміть код з заняття і доопрацюйте натупним чином:
# користувач має вгадати чизло за певну кількість спроб. користувач на початку програми визначає кількість спроб
# додайте підказки. якщо рвзнися між числами більше 10 - "холодно", від 10 до 5 - "тепло", 1-4 - "гаряче"

from random import randint


def get_ai_number():
    number = randint(1, 100)
    # print(f'AI: {number}')
    return number


def get_user_number():

    while True:
        try:
            return int(input('Enter the number (int): '))
        except ValueError:
            print('Number please!')


def check_numbers(ai_number, user_number):
    if abs(user_number - ai_number) > 10:
        print('Cold\n')
        return False
    elif abs(user_number - ai_number) in range(5, 11):
        print('Warm\n')
        return False
    elif abs(user_number - ai_number) in range(1, 5):
        print('Hot\n')
        return False
    print('Guessed')
    return True


def attempts():
    while True:
        try:
            return int(input('Enter the number of attempts: '))
        except ValueError:
            print('Number please!')

def game_guess_number():
    print('Game begins!')

    num_of_attempts = attempts()

    ai_number = get_ai_number()

    counter = 0
    while counter < num_of_attempts:
        print(f'Attempt №{counter+1}')
        user_number = get_user_number()
        is_game_end = check_numbers(ai_number, user_number)

        if is_game_end:
            break
        counter += 1

    print('User win')

print('\n\n\t\t Task 2')
game_guess_number()
