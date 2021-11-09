# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def devide_two_num():
    try:
        num1 = int(input("введите число"))
        num2 = int(input("введите число"))
    except ValueError:
        return

    """вариант 1"""
    # try:
    #     dev_t_n=num1/num2
    # except ZeroDivisionError:
    #     dev_t_n="нельзя делить на ноль"
    """вариант 2"""
    if num2 !=0:
        dev_t_n = num1 / num2
    else: dev_t_n="нельзя делить на ноль"
    return dev_t_n

print(f'результат: {devide_two_num()}')

