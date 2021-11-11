# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания,
# email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def user_data1(**kwargs):
    return kwargs
print('вариант 1')
print(user_data1(name="iv", surname="iva", year=1999, town="moscow", email="email", phone=12345))


def user_data2(name, surname, year, town, email, phone):
    return print(f'имя:{name} фамилиия:{surname} год рождения:{year} город:{town} email:{email} телефон:{phone}')
print('вариант 2')
user_data2('иван','иванов',1999,'иваново', 'ываыва', 12312)

