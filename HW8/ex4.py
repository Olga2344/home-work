# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите
# параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для
# каждого типа оргтехники.
# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники
# на склад и передачу в определённое подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру
# (например, словарь).
# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class Warehouse:
    def __init__(self, amount_of_shelves, amount_of_levels):
        self.amount_of_shelves = amount_of_shelves
        self.amount_of_levels = amount_of_levels
        # storege= '''сделать матрицу хранения'''

    def accept_item(self):
        pass

    def issue_item(self):
        pass


class Equipment:
    def __init__(self, brand, serial_number):
        self.brand = brand
        self.serial_number=serial_number

    def action(self):
        pass

class Printer(Equipment):
    def __init__(self, brand, func,serial_number):
        super().__init__(brand, serial_number)
        self.func = func

    def action(self):
        print('печатает')


class CopyCenter(Equipment):
    def __init__(self, brand, func, serial_number):
        super().__init__(brand, serial_number)
        self.func = func

    def action(self):
        print('копирует')


class Laptop(Equipment):
    def __init__(self, brand, serial_number, func, ):
        self.func = func
        super().__init__(brand, serial_number)

    def action(self):
        print('работает')