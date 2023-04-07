# Напишіть функцію, яка визначає сезон за датою. Функція отримує стрінг у форматі
# "[день].[місяць]" (наприклад "12.01", "30.08", "1.11" і тд) і повинна повернути стрінг з
# відповідним сезоном, до якого відноситься ця дата ("літо", "осінь", "зима", "весна")

def get_season(date_str):
    """
    Функція, яка визначає сезон за датою.

    Аргументи:
    date_str (str): Рядок, що містить день та місяць в форматі "день.місяць".

    Повертає:
    str: Сезон, до якого відноситься дата ("зима", "весна", "літо" або "осінь").
    """

    date_list = date_str.split('.')

    if int(date_list[1]) == 12 or int(date_list[1]) <= 2:
        return 'зима'
    elif int(date_list[1]) in range(3, 6):
        return 'весна'
    elif int(date_list[1]) in range(6, 9):
        return 'літо'
    elif int(date_list[1]) in range(9, 12):
        return 'осінь'


print(get_season('13.06'))

# Напишіть функцію "Тупий калькулятор", яка приймає два числових аргументи і строковий,
# який відповідає за операцію між ними (+ - / *). Функція повинна повертати значення відповідної операції
# (додавання, віднімання, ділення, множення), інші операції не допускаються. Якщо функція оримала невірний тип данних для
# операції (не числа) або неприпустимий (невідомий) тип операції вона повинна повернути None і
# вивести повідомлення "Невірний тип даних" або "Операція не підтримується" відповідно

def stupid_calculator(num1, num2, operation):
    """
    Функція, що виконує операції додавання, віднімання, множення та ділення на два числових аргументи.

    Аргументи:
    num1 (int, float): Перший числовий аргумент.
    num2 (int, float): Другий числовий аргумент.
    operation (str): Рядок, який відповідає за операцію між двома аргументами.
                     Приймає значення '+', '-', '*', '/'.

    Повертає:
    int або float: Результат операції між двома аргументами.

    Або повертає None, якщо операція невідома або аргументи не є числами.
    """

    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        print("Невірний тип даних")
        return None

    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            print("Ділення на 0")
            return None
        return num1 / num2

    print("Операція не підтримується")
    return None

print(stupid_calculator(5,4,"+"))
