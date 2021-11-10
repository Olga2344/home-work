# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
"""вариант 1"""
# def my_func_summ():
#     try:
#         num1 = int(input("введите число"))
#         num2 = int(input("введите число"))
#         num3 = int(input("введите число"))
#     except ValueError:
#         return
#     if num1>=num3 and num2>=num3:
#         sun_num=num1+num2
#     elif num3>num1 and num2>num1:
#         sun_num = num3 + num2
#     else: sun_num=num1+num3
#
#     return sun_num
#
# print(f'результат: {my_func_summ()}')

"""вариант 2"""
def my_func_summ(num1,num2,num3):
    list_nums=[num1,num2,num3]
    list_nums.remove(min(list_nums))
    return sum(list_nums)
print(my_func_summ(1,1,1))
