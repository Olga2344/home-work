# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class ChekData:
    def __init__(self, data):
        self.data = data

    @classmethod
    def transform_to_int(cls, data):
        return [int(i) for i in data.split("-")]

    @staticmethod
    def chek_date(data):
        transform_to_int=[int(i) for i in data.split("-")]
        if len(transform_to_int)==3:
            if (0<transform_to_int[0]<31) and(0<transform_to_int[1]<13) and(transform_to_int[2]>0):
                return data
            else:
                return f"неверный формат даты"


print(ChekData.transform_to_int('12-2-1234'))
print(ChekData.chek_date('12-12-1234'))
