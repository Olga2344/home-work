# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car():

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        return f'текущая скорость {self.speed} машины {self.name}'

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn(self, direction):
        if direction == 'left':
            return f'{self.name} повернула налево'
        elif direction == 'right':
            return f'{self.name} повернула направо'
        else:
            return f'не введено направление'


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed >= 60:
            return f'Машина {self.name} Вы превысили сорость 60'
        else:
            return f'текущая скорость {self.speed} машины {self.name}'


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)

    def show_speed(self):
        if self.speed >= 40:
            return f'Машина {self.name} Вы превысили сорость 40'
        else:
            return f'текущая скорость {self.speed} машины {self.name}'


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car_1 = TownCar(80, 'rr', 'ee')
car_2 = TownCar(90, 'ww', 'ff')
car_3 = SportCar(30,'aa','dd')
car_4 = PoliceCar(100,'ss', 'PP')
car_5 = WorkCar(50, 'hh','WW')
print(car_2.show_speed())
print(car_3.show_speed())
print(car_4.show_speed())
print(car_5.show_speed())
print(car_5.stop())
print(car_2.turn('left'))
print(car_4.turn('right'))
print(car_3.go())

