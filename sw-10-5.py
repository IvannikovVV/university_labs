class NameLengthError(Exception):
    def __init__(self, message):
        self.message = message

def lower_case_username(value):
    if len(value) < 6:
        raise NameLengthError('Длина имени должна быть больше шести символов')

class Student:
    def __init__(self, name, age):
        self.name = lower_case_username(name)
        self.age = age

try:
    lower_case_username('Вий')
except NameLengthError as err:
    print('Ошибка:', err)

try:
    Student('Лика', 31)
except NameLengthError as err:
    print('Ошибка:', err)

try:
    Student('Виктор', 27)
except NameLengthError as err:
    print('Ошибка:', err)
finally:
    print('Учётная запись работника создана успешно')