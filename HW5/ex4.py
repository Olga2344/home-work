# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
eng_dict={'One':'один', 'Two':'Два', 'Three':'Три', 'Four':'Четрыре'}
with open(r"text_files/text4.txt", 'r') as f_obj:
    for line in f_obj:
        line=line.strip()
        temp_list=line.split(' ')
        with open (r"text_files/text4_1.txt", 'a') as f_obj:
            if temp_list[0] in eng_dict.keys():
                temp_list1=(str(eng_dict.setdefault(temp_list[0]))+ ' ' + ' '.join(temp_list[1::]))
                print(temp_list1, file=f_obj)