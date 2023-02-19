# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def exponentiation(a, b):
    exp = 1
    while b != 0:
        exp = exp * a
        b -= 1
        exponentiation(a, b)
    return exp

a = int(input('Введите число, возводимое в степень: '))
b = int(input('Введите степень: '))

print(f' Число {a} в степени {b}  = {exponentiation(a,b)}')