# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
# и возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее
# функцию int_func().

def int_func(t):
    t1=t.capitalize()
    return t1
print('вариант 1')
print(int_func('text'))

def int_func1(t):
    t1=t.split()
    t2=[]
    t3=()
    for elem in t1:
        t2.append(elem.capitalize())
    t3=','.join(t2)

    return t3
print('вариант 2')
print(int_func1('text0 text1 text2 text3 '))
