#Є list довільних чисел, наприклад [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]. Напишіть код, \
# який видалить (не створить новий, а саме видалить!) з нього всі числа, які менше 21 і більше 74.
print("\t\tTask 1")
lst = [11, 77, 4, 22, 0, 56, 5, 95, 7, 5, 87, 13, 45, 67, 44]

i = 0
while i < len(lst):
    if lst[i] not in range(21, 75):
        del lst[i]
    else:
        i += 1

print(lst)

#Є два довільних числа які відповідають за мінімальну і максимальну ціну. Є Dict з назвами магазинів і цінами:\
# { "citos": 47.999, "BB_studio" 42.999, "mo-no": 49.999, "my-main-service": 37.245, "buy-now": 38.324,\
# "x-store": 37.166, "the-partner": 38.988, "store-123": 37.720, "roze-tka": 38.003}. \
# Напишіть код, який знайде і виведе на екран назви магазинів, ціни яких потрапляють в діапазон між мінімальною і \
# максимальною ціною.
import re

def do_input_float(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[-+]?[0-9]{1,}(\.[0-9]{1,})?$', value)):
            flag = False
            value = float(value)
        else:
            print('error')
    return value

dict1 = {
    "citos": 47.999,
    "BB_studio": 42.999,
    "mo-no": 49.999,
    "my-main-service": 37.245,
    "buy-now": 38.324,
    "x-store": 37.166,
    "the-partner": 38.988,
    "store-123": 37.720,
    "roze-tka": 38.003
}

print("\n\t\tTask 2")
lower_limit = do_input_float("Введіть нижню ціну:")

while True:
    upper_limit = do_input_float("Введіть верхню ціну:")
    if lower_limit > upper_limit:
        print("Верхня межа повинна бути більше ніж нижня")
    else:
        break

markets = [key for key, value in dict1.items() if lower_limit <= value <= upper_limit]

print("Matches:", ", ".join(markets))

