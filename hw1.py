#Задача: Створіть дві змінні first=10, second=30. Виведіть на екран результат математичної взаємодії\
#(+, -, *, / и тд.) для цих чисел.

first, second = 10, 30
print(f'\t\tTask 1\nДодавання:{first + second}\nВіднімання first від second:{second - first}\nВіднімання second від \
first:{first - second}\nМноження:{first*second}\nДілення first на second:{first/second}\n\
Ділення second на first:{second/first}\nfirst^second:{first**second}\nsecond^first:{second**first}')

#Задача: Створіть змінну и по черзі запишіть в неї результат порівняння (<, > , ==, !=)\
# чисел з завдання 1. Виведіть на екран результат кожного порівняння.
bool_list = []
bool_list.append(first > second)
bool_list.append(first < second)
bool_list.append(first == second)
bool_list.append(first != second)
print(f'\t\tTask 2\n\
first > second:{bool_list[0]}\n\
first < second:{bool_list[1]}\n\
first == second:{bool_list[2]}\n\
first != second:{bool_list[3]}\n')

#Задача: Створіть змінну - резкльтат конкатенації строк "Hello " та "world!"
hello_str = 'Hello ' + 'world!'
print(f'\t\tTask 3\n\
{hello_str}')
