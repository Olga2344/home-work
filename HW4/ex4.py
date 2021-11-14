# 4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.
from random import randrange
num_list = [randrange(1, 10) for i in range(15)]
print(num_list)
original_num_list=[num_list[i] for i in range(len(num_list)) if num_list.count(num_list[i]) <=1]
print(original_num_list)