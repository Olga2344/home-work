# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число». Реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта. Для этого создаёте экземпляры класса (комплексные числа),
# выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
from itertools import count


class ComplexNumber:
    _ids = count(1)

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.id = next(self._ids)

    def __str__(self):
        return f'z{self.id} = {self.a} + {self.b}j'

    def __add__(self, other):
        a_1 = self.a + other.a
        b_1 = self.b + other.b
        return ComplexNumber(a_1, b_1)

    def __mul__(self, other):
        a_1 = self.a * other.a - self.b * other.b
        b_1 = self.a * other.b + self.b * other.a
        return ComplexNumber(a_1, b_1)


z1 = ComplexNumber(1, 3)
z2 = ComplexNumber(5, 2)
z3 = z1 + z2
z4 = z1 * z2

print(z1)
print(z2)
print(z3)
print(z4)
