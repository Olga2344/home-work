#5. Создать (программно) текстовый файл,
# записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
sum_num=0
numbers=[]
with open(r"text_files/text3.txt", 'w') as f_obj:
    values = ' '.join(str(v) for v in range(0, 10))
    print(values, file=f_obj)

with open(r"text_files/text3.txt", 'r') as f_obj:
    for line in f_obj:
        numbers=map(int, line.split())
    for id, val in enumerate(numbers):
        sum_num += val
    print(f'сумма числе в файле: {sum_num}')