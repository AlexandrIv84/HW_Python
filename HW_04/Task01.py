# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания
# все те числа, которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во элементов первого множества.
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите количество элементов первого множества: '))
nabor_1 = []
nabor_2 = []
for _ in range(n):
    nabor_1.append(input('Введите элемент:  '))

m = int(input('Введите количество элементов второго множества: '))
for _ in range(m):
    nabor_2.append(input('Введите элемент:  '))
print(f' Первый набор цифр: {nabor_1}')
print(f' Второй набор цифр: {nabor_2}')
nabor_final = []
for item in nabor_1:
    if item in nabor_2:
        nabor_final.append(item)
nabor_final = set(nabor_final)
list(nabor_final).sort()
print(f'Полученный список цифр: {nabor_final}')