# Пользователь вводит число от 1 до 9999 (сумму выдачи в банкомате).
# Необходимо вывести на экран словами введенную сумму
# и в конце написать название валюты с правильным окончанием.

def text_with_num(num: int, text: list) -> str:
    which = -1
    which += num % 10 == 1 and num % 100 != 11
    which += 2 <= num % 10 <= 4 and \
             (num % 100 < 10 or num % 100 >= 20) and 2
    return f'{text[which]}'


RUS = {
    0: [''], 1: ['один', 'одна'],
    2: ['два', 'две'], 3: ['три'],
    4: ['четыре'], 5: ['пять'],
    6: ['шесть'], 7: ['семь'],
    8: ['восемь'], 9: ['девять'],
    10: ['десять', 'десят'],
    11: ['одиннадцать'], 12: ['двенадцать'],
    13: ['тринадцать'], 14: ['четырнадцать'],
    15: ['пятнадцать'], 16: ['шестнадцать'],
    17: ['семнадцать'], 18: ['восемнадцать'],
    19: ['девятнадцать'], 20: ['двадцать'],
    30: ['тридцать'], 40: ['сорок'],
    90: ['девяносто'], 100: ['сто', 'ста', 'сот'],
    200: ['двести'], 1000: ['тысяча', 'тысячи', 'тысяч'],
    '$': ['доллар', 'доллара', 'долларов'],
}

amount = int(input('Введите сумму: '))
phrase = ''

thousands = amount // 1000
if thousands:
    phrase += RUS[thousands][-1] + ' '
    phrase += text_with_num(thousands, RUS[1000])

phrase = phrase.strip() + ' '

hundreds = amount // 100 % 10
if hundreds:
    phrase += RUS.get(hundreds * 100, [False])[0] or\
              RUS[hundreds][-1] + \
              RUS[100][1 + hundreds // 5]

phrase = phrase.strip() + ' '

tens = amount % 100
if tens < 20:
    phrase += RUS.get(tens, [False])[0] or ''
else:
    phrase += RUS.get(tens // 10 * 10, [False])[0] or\
              RUS[tens // 10][0] + RUS[10][1]

    phrase = phrase.strip() + ' '
    tens = tens % 10
    phrase += RUS[tens][0]

phrase = phrase.strip() + ' '
phrase += text_with_num(amount, RUS['$'])
phrase = phrase.capitalize()

print(phrase)

# Введите сумму: 7431
# > Семь тысяч четыреста тридцать один доллар

# Введите сумму: 2149
# > Две тысячи сто сорок девять долларов

# Введите сумму: 15
# > Пятнадцать долларов

# Введите сумму: 3
# > Три доллара
