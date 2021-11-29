#3. Создать текстовый файл (не программно),
# построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.
workers_list={}
poor_workers=[]
sum_salary=0
with open(r"text_files/text2.txt", 'r') as f_obj:
    for line in f_obj:
        workers_list[line.split(' ')[0]]=int(line.split(' ')[1])
for key, value in workers_list.items():
    sum_salary+=value
    if value<=20000:
        poor_workers.append(key)

print(f"список сотрудников с окладом менее 20 тыс.: {', '.join(poor_workers)}." )
print(f'средняя заработная плата={sum_salary/len(workers_list)}')
