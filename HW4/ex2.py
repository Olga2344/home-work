# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randrange

num_lisi = [randrange(1, 200) for i in range(15)]
print(num_lisi)
sorted_num_list = [num_lisi[i] for i in range(len(num_lisi) - 1) if num_lisi[i] > num_lisi[i + 1]]
print(sorted_num_list)
