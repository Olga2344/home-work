# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор
# натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
new_elem=int(input('новый элемент рейтинга: '))
my_list = [9, 7, 5, 5, 2]
for x in range(0, len(my_list), 1):
    if my_list[x]<new_elem:
        my_list.insert(x,new_elem)
        break
    else: my_list.append(new_elem)
    break
print(my_list)