# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход,
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

import random
n = int(input('Введите количество кустов: '))
bushes =[]
for _ in range(n):
    bushes.append(random.randint(0, 10))
print(bushes)
berries =[]
for i in range(n):
    next = i + 1
    previus = i - 1
    if i == 0:
        previus = -1
    elif i == n-1:
        next = 0
    berries.append(bushes[previus] + bushes[i] + bushes[next])

print(f'Максимальное число ягод при сборке = {max(berries)}')