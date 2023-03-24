#Hапишіть цикл, який буде вимагати від користувача ввести слово, в якому є буква "о" \
# (враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "о".

while True:
    word = input('Введіть слово з буквой \'о\':')
    if 'o' in word.lower() or 'о' in word.lower(): #кирилична і латинська о
        print('Ви дійсно ввели слово з буквой о:', word)
        break
    print('Слово без о')

#Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. Напишіть код, \
# який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. Зауважте, що \
# lst1 не є статичним і може формуватися динамічно від запуску до запуску.

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = list(filter(lambda x: isinstance(x, str), lst1))
print(lst2)

#Є стрінг з певним текстом (можна скористатися input або константою). Напишіть код, який визначить кількість слів\
# в цьому тексті, які закінчуються на "о" (враховуються як великі так і маленькі).
import string

input_str = input('Введіть текст:')
#Видаляємо всі знаки пунктуації крім апострофа
input_str = "".join([word for word in input_str if word not in string.punctuation or word == "'"])
words_list = input_str.split()

count = 0
for word in words_list:
    if word.lower().endswith('o') or word.lower().endswith('о'): #кирилична і латинська 'о'
        count += 1


print('\nК-сть слів, що закінчуються на о:', count)

