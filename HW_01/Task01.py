# Задание № 1
# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

n = int(input('Введите целое трехзначное число: '))
if 99 < n < 1000:       # Другие проверки не стал делать
    summa = 0
    while n > 0:
        summa += n % 10
        n = n // 10
    print('Сумма цифр данного числа = ', summa)
else:
    print('Вы ввели число не удовлетворяющее условию!')

