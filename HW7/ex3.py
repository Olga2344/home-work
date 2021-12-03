# Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
# вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться
# только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.

class CellCulture:

    def __init__(self, name, quantity):
        self.quantity = quantity
        self.name = name

    def __add__(self, other):
        added_cell = self.quantity + other.quantity
        return f'{self.name} and {other.name} added. Contain {added_cell} cells'

    def __sub__(self, other):
        if self.quantity > other.quantity:
            dif_cell = self.quantity - other.quantity
            return f'{other.name} kill {self.name}, survive {dif_cell} from {other.name}'
        elif self.quantity == other.quantity:
            return f'{self.name} and {other.name} destroyed each other'
        else:
            dif_cell = other.quantity - self.quantity
            return f'{self.name} kill {other.name}, survive {dif_cell} from {self.name}'

    def __mul__(self, other):
        return f'Multiplied cell culture contains {self.quantity * other.quantity} cells'

    def __truediv__(self, other):
        return f'Divided cell culture is alternative biology, but now it contains {self.quantity // other.quantity} cells'

    def make_order(self, cell_in_row):
        self.cell_in_row = cell_in_row
        row=self.quantity // cell_in_row
        unit_in_row = ''
        total_cell = self.quantity

        # for i in range(self.quantity // cell_in_row):
        #     unit_in_row += '*' * cell_in_row + '\n'
        # unit_in_row += '*' * (self.quantity % cell_in_row)

        for r in range(self.quantity // cell_in_row):
            if total_cell >= cell_in_row:
                for i in range(self.cell_in_row):
                    unit_in_row += '*'
                total_cell -= cell_in_row
                unit_in_row += '\n'
        for i in range(total_cell):
            unit_in_row += '*'

        return f'\nUnit whith cells looks like\n{unit_in_row}'


new_cell = CellCulture('E.coil', 2)
new_cell_1 = CellCulture('B.coil', 10)
q = new_cell - new_cell_1
d = new_cell / new_cell_1
a = new_cell + new_cell_1
m = new_cell * new_cell_1
print(q)
print(d)
print(a)
print(m)
print(new_cell.make_order(3))
