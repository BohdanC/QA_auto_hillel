import re

#Сформуйте стрінг, в якому міститься інформація про певне слово. "Word [тут слово] has [тут довжина слова,\
# отримайте з самого сдлва] letters", наприклад "Word 'Python' has 6 letters". Для отримання слова для аналізу\
# скористайтеся константою або функцією input().

word = input("Choose word u want to check:")
word_construction = f'Word \'{word}\' has {len(word)} letters'
print(word_construction)

#Напишіть программу "Касир в кінотеватрі", яка попросіть користувача ввести свсвій вік\
# (можно використати константу або функцію input(), на екран має бути виведено лише одне повідомлення,\
# також подумайте над варіантами, коли введені невірні дані).
#        якщо користувачу менше 7 - вивести повідомлення"Де твої батьки?"
#        якщо користувачу менше 16 - вивести повідомлення "Це фільм для дорослих!"
#        якщо користувачу більше 65 - вивести повідомлення"Покажіть пенсійне посвідчення!"
#        якщо вік користувача містить цифру 7 - вивести повідомлення "Вам сьогодні пощастить!"
#        у будь-якому іншому випадку - вивести повідомлення "А білетів вже немає!"


def do_input_int(message):
    flag = True
    while flag:
        value = input(message)
        if bool(re.match('^[0-9]{1,}$', value)):
            flag = False
            value = int(value)
        else:
            print('Not valid value')
    return value

age = do_input_int('How old are u?:')

if age < 7:
    print("Where are your parents?")
elif '7' in str(age):
    print("U are lucky today")
elif 7 <= age < 16:
    print("This is a movie for adults")
elif age > 65:
    print("Show your retirement certificate")
else:
    print('No tickets has left yet')



