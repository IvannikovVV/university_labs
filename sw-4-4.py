def calc(*numbers):
    countNumbers = len((numbers))
    result = 0;
    for i in range(countNumbers):
        result += numbers[i]

    return result / countNumbers

def main():
    print('Для числе 1, 5 и 9 среднее арифметическое будет:', calc(1, 5, 9))

if __name__ == '__main__':
    main()