# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

n = int(input('Введите количество монеток: '))
coin = [0]*n
heads = tails = 0
for i in range(n):
    coin[i] = randint(0,1)
    if coin[i] == 1:
        heads +=1
    else:
        tails +=1
print(coin)
print(f' Орел: {heads} шт.')
print(f' Решко: {tails} шт.')
print(f' Необходимо перевернуть {min(heads, tails)} монеток')