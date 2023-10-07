value = input('Введите предложение: ')

print('Длина предложения:', len(value))
print('Предложение в нижнем регистре:', value.lower())

words = 0
for i in range(len(value)):
    if value[i] in ['a', 'e', 'i', 'o', 'u']:
        words += 1
print('Количество гласных в предложении:', words)

print('Замена "ugly" на "beauty":', value.replace('ugly', 'beauty'))
print('Предложение начинается на well:', 'да' if value.find('Well') == 0 else 'нет')
print('Предложение заканчивается на com:', 'да' if value.find('com') == len(value) - len('end') else 'нет')