# -*- coding: utf-8 -*-
from sys import argv
print(int(argv[1]) * int(argv[2]) + int(argv[3]))
print(f"salary = {int(argv[1]) * int(argv[2]) + int(argv[3])}")
# если пиать в таком виде print(f' salary = {int(argv[1]) * int(argv[2]) + int(argv[3])}'),
# то выдает ошибку SyntaxError: invalid syntax на кавычки
