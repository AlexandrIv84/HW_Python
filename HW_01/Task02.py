# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

n = int(input('Введите количество журавликов: '))
if n > 0 and n % 6 == 0:
    print(f'Петя сделал журавликов: {round(n / 6)}')
    print(f'Сережа сделал журавликов: {round(n / 6)}')
    print(f'Катя сделала журавликов: {round(n / 1.5)}')
else:
    print('При таком количестве задача не решаема')