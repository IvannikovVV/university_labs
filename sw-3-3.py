value = int(input('Введите число от 0 до 10 включительно: '))

if value >= 0 and value <= 3:
    print('от 0 до 3 включительно')
elif value > 3 and value < 6:
    print('от 3 до 6')
elif value >= 6 and value <= 10:
    print('от 6 до 10 включительно')
else:
    print('Указано некорректное значение')