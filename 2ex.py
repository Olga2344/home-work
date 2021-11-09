# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list=input('введите несколько слов: ').split()
print(my_list)
my_list_len= len(my_list)
if my_list_len%2 == 0 :
    my_list_len=my_list_len-1
else:
    my_list_len=my_list_len-2

for i in range(0, my_list_len, 2):
    my_list[i], my_list[i+1]=my_list[i+1], my_list[i]

print(my_list)