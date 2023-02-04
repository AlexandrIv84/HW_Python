# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

from random import randint

number1 = randint (1, 1001)
number2 = randint (1, 1001)
n = m = 0
print(f'Петя загадал два числа. (Первое число {number1}, а второе {number2}, тссссс... только никому не говори!)')
print(f'Сумма этих чисел = {number1 + number2}, а произведение = {number1 * number2} ')
print('Попробуй угадай! у тебя 5 попыток')
for _ in range(5):
    # print(type(n))
    # print(type(number1))
    n = int(input('Введи первое число: '))
    m = int(input('Введи второе число: '))
    # print(f'{n} {m}')
    if (n == number1 and m == number2) or (n == number2 and m == number1):
        print('')
        print('***Молодец, ты умная Катя!***')
        break
    else:
        print('Не угадал, попробуй снова')
else:
    print('')
    print('**Увы, попытки закончились**(')

