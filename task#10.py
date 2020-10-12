# -*- coding: utf-8 -*-

# Условие: Python напился, и в результате встроенные функции str()
# и int() ведут себя странно:
# str(4) ➞ 4
# str("4") ➞ 4
# int("4") ➞ "4"
# int(4) ➞ "4"

# Вам нужно создать две функции, заменяющие str() и int().
# Функция int_to_str() должна конвертировать целые числа в строки,
# а функция str_to_int() —  строки в целые числа.

# Примеры:
# int_to_str(4) ➞ "4"
# str_to_int("4") ➞ 4
# int_to_str(29348) ➞ "29348"


def int_to_str(digit):
   return f"{digit}".__repr__()

def str_to_int(string):
   return eval(string)


print(int_to_str(4))
print(str_to_int("4"))