# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    exponen=x**y
    return exponen
print('вариант 1')
print(my_func1(2,-4))

def my_func2(x, y):
    i=-1
    exponen=x
    while i>y:
        exponen=exponen*x
        i -= 1
    return 1/exponen
print('вариант 2')
print(my_func2(2,-4))




