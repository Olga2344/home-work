# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

class Matrix():
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __str__(self):
        n_m = list()
        n_m1 = str()

        for line in self.list_of_list:
            for i, v in enumerate(line):
                n_m.append(v)
                if i == len(line) - 1:
                    n_m.append('\n')
                n_m1 = '\t'.join(map(str, n_m))

        return f'\t{n_m1}'

    def __add__(self, other):
        nw_mtrx = [[0 for x in range(len(self.list_of_list[0]))] for y in range(len(self.list_of_list))]

        if len(self.list_of_list) == len(other.list_of_list):
            if len(self.list_of_list[0]) == len(other.list_of_list[0]):
                for i in range(len(self.list_of_list)):
                    for j in range(len(self.list_of_list[i])):
                        nw_mtrx[i][j] = self.list_of_list[i][j] + other.list_of_list[i][j]

                return f'new Matrix\n{Matrix(nw_mtrx)}'
        else:
            return f'Invalid matrix size'


my_matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 2, 1]])

my_matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1], [3, 2, 1]])

n_mt = my_matrix1 + my_matrix2
print(n_mt)

print(my_matrix1)
print(my_matrix2)