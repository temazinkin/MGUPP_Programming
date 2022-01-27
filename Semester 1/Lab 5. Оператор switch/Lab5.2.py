# Изменить код, который был рассмотрен в примере, следующим образом:
# Пользователю для расчета времени в пути надо вводить не номера станций,
# а буквы (A,B,C,D,E). Необходимо предусмотреть ввод пользователем и маленьких,
# и больших букв (избавиться от регистрозависимости).
# То есть если введено или D, или d — должен сработать один и тот же case.

a = input()
b = True

while b:
    if a in 'Aa':
        print('Trinitat Nova')
        print('15 мин')
        b = False
    elif a in 'Bb':
        print("Casa de l'Aigua")
        print('19 мин')
        b = False
    elif a in 'Cc':
        print('Torre Baro Vallbona')
        print('25 мин')
        b = False
    elif a in 'Dd':
        print('Ciutat Meridiana')
        print('30 мин')
        b = False
    elif a in 'Ee':
        print('Can Cuias')
        print('38 мин')
        b = False
    else:
        print('Станции нет')
        a = input()
