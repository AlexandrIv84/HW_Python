# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum(a, b, summa):
    # summa = 0
    if a != 0:
        a -= 1
        summa += 1
        # print(f' a  = {a}')
        # print(f' сумма  = {summa}')

        sum(a, b, summa)
    elif b != 0:
        b -= 1
        summa += 1
        # print(f' b  = {b}')
        # print(f' сумма  = {summa}')
        sum(a, b, summa)
    else:
        print(f'Сумма чисел  = {summa} ')


a = int(input('Введите число А: '))
b = int(input('Введите число B: '))
summa = 0
sum(a, b, summa)