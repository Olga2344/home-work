# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

"""вариант 1"""
# def user_data(**kwargs):
#     return kwargs
# print(user_data(name="iv", surname="iva", year=1999, town="moscow", email="email", phone=12345))
"""вариант 2"""
def user_data(name, surname, year, town, email, phone):
    return print(f'имя:{name} фамилиия:{surname} год рождения:{year} город:{town} email:{email} телефон:{phone}')
user_data('иван','иванов',1999,'иваново', 'ываыва', 12312)

