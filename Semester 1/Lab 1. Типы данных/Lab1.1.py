# Объявить переменные, с помощью которых можно будет посчитать
# общую сумму покупки нескольких товаров (цена + количество товара).
# Например, плитки шоколада, кофе и пакеты молока.

price_choco, quantity_choco = 172.99, 4
price_coffee, quantity_coffee = 599.99, 7
price_milk, quantity_milk = 98.5, 3

amount = price_choco * quantity_choco
amount += price_coffee * quantity_coffee
amount += price_milk * quantity_milk

print(f'{amount:.02f}')
# > 5187.39
