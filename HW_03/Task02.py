# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
dictionary = {1:  'AEIOULNSTRАВЕИНОРСТ',
              2:  'DGДКЛМПУ',
              3:  'BCMPБГЁЬЯ',
              4:  'HVWYЙЫ',
              5:  'KЖЗХЦЧ',
              8:  'JXШЭЮ',
              10: 'QZФЩЪ'}

str = input('Введите слово:  ')
sum = 0

for letter in str:
    for key, value in dictionary.items():
        if letter.upper() in value:
            sum += key

print(f'Сумма очков слова {str} = {sum}')