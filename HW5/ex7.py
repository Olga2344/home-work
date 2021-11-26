# 7. Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
profit=0
count_firm=0
average_profit=0
average_dict={}
firm_dict={}
with open(r"text_files/text7.txt", 'r') as f_obj:
    for line in f_obj:
        line=line.split(' ')
        profit=int(line[2])-int(line[3])
        firm_dict[line[0]] = profit
        if profit >=0:
            average_profit+=profit
            count_firm+=1
    average_dict["average_profit"]=average_profit/count_firm
    print(average_dict)
    print(firm_dict)

with open(r"text_files/my_file.json", "w") as write_f:
    json.dump([average_dict, firm_dict], write_f)
