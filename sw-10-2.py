class EmptyFileError(Exception):
    def __init__(self, message):
        self.message = message

def open_file(path, mode):
    try:
        with open(path, mode) as file:
            content = file.read()
            if content == '':
                raise EmptyFileError('Этот файл пустой')
            else:
                print('Содержимое этого файла:', content)
    except EmptyFileError as err:
        print('Внимание! Ошибка:', err)

open_file('./static/sw-10-2-1_empty_file.txt', 'r')
open_file('./static/sw-10-2-2_filled_file.txt', 'r')