# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def amount_of_fabric(self):
        pass


class Sute(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    @property
    def amount_of_fabric(self):
        return (self.size / 6.5) + 0.5


class Coat(Clothes):
    def __init__(self, name, higt):
        super().__init__(name)
        self.higt = higt

    @property
    def amount_of_fabric(self):
        return (self.higt * 2) + 0.3


new_coat = Coat('from market', 2)
new_sute = Sute('from shop', 4)

print(new_coat.amount_of_fabric)
print(new_sute.amount_of_fabric)

total_f=new_coat.amount_of_fabric+new_sute.amount_of_fabric
print(total_f)
