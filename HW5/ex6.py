# 6. Необходимо создать (не программно) текстовый файл,
# где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
item_dict={}

with open(r"text_files/text6.txt", 'r') as f_obj:
    for line in f_obj:
        sum_hours = 0
        line=line.replace(':','')
        line=line.split(' ')
        for i in line[1::]:
            i=i.split('(')
            try:
                if int(i[0]) == True:
                    sum_hours = sum_hours + int(i[0])
            except:
                continue
            else:
                sum_hours=sum_hours+int(i[0])
        item_dict[line[0]]=sum_hours
    print(item_dict)