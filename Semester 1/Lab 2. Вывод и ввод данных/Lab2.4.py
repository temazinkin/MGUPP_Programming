# Пользователь должен ввести 2 числа.
# Вам надо показать на экран произведение этих чисел, сумму и разницу.
# Покажите также среднее арифметическое этих введенных чисел.

first = int(input('Первое число: '))
second = int(input('Второе число: '))

multiply = first * second
add = first + second
subtract = first - second
average = add / 2

print(f'Произведение {multiply}')
print(f'Сумма {add}')
print(f'Разница {subtract}')
print(f'Сред.арифметическое {average}')

# Первое число: 5
# Второе число: 4
# > Произведение 20
# > Сумма 9
# > Разница 1
# > Сред.арифметическое 4.5
