example_1 = (1, 10, 8, 5, 4, 69, 71, 88, 1, 101)
example_2 = (24, 9, 354, 310781, 566, 777, 8)
example_3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

def get_even_numbers(values):
    new_list = []

    for x in list(values):
        if x % 2 == 0: new_list.append(x)

    return tuple(new_list)

print('Пример 1:', get_even_numbers(example_1))
print('Пример 2:', get_even_numbers(example_2))
print('Пример 3:', get_even_numbers(example_3))