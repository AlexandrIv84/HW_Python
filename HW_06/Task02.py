# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

n = int(input('Введите количество элементов списка: '))
list_numbers = []
for _ in range(n):
    list_numbers.append(random.randint (-10, 30))
print(list_numbers)

start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))

for i in range(len(list_numbers)):
    # print(start)
    # print(end)
    # print(f'    {list_numbers[i]}')
    if start <= list_numbers[i] <= end:
        print(f'Индекс числа {list_numbers[i]}, входящего в диапазон = {i}')