# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

from random import randint

n = int(input('Введите длину списка: '))

list_numbers = []
for _ in range(n):
    list_numbers.append(randint(0, 100))
print(list_numbers)

x = int(input('Введите искомое число Х: '))
near = list_numbers[0]
counter = 0
for i in range(n):
    if list_numbers[i] == x:
        counter += 1
if counter > 0:
    print(f'Число встречается {counter} раз')
else:
    for number in list_numbers:
        if abs(x - number) < abs(x - near):
            near = number
    print(f'Ближайшее число = {near}')
