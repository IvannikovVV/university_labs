with open('static/sw-7-2.txt', 'a') as file:
    date = input('Введите дату: ')
    category = input('Введите категорию: ')
    sum = int(input('Введите сумму: '))

    file.write(f'{date}\t\t\t{category}\t\t\t{sum}\n')

with open('static/sw-7-2.txt', 'r') as file:
    print('Учёт расходов:\n', file.read())