# 1. Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

with open(r"text_files/text1.txt", 'w') as f_obj:
    while True:
        input_str = input('введите строку: ')
        if len(input_str) == 0:
            break
        else:
            print(input_str, file=f_obj)
