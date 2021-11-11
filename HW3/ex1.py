# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide_two_num1():
    try:
        num1 = int(input("введите число"))
        num2 = int(input("введите число"))
    except ValueError:
        return

    if num2 !=0:
        dev_t_n = num1 / num2
    else: dev_t_n="нельзя делить на ноль"
    return dev_t_n
print('вариант 1')
print(f'результат: {devide_two_num1()}')

def devide_two_num2():
    try:
        num1 = int(input("введите число"))
        num2 = int(input("введите число"))
    except ValueError:
        return

    try:
        dev_t_n=num1/num2
    except ZeroDivisionError:
        dev_t_n="нельзя делить на ноль"
    else: dev_t_n=num1/num2
    return dev_t_n
print('вариант 2')
print(f'результат: {devide_two_num2()}')

