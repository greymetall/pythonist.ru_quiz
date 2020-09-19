# -*- coding: utf-8 -*-

# Условие: Repdigit это положительное число, для записи которого
# используются одинаковые цифры. Создайте функцию, которая будет
# принимать число и определять, repdigit это или нет.
# Функция должна возвращать True или False.

# Примечание: При введении нуля должно возвращаться True
# (хотя нуль и не является положительным числом).

# Примеры: 
# is_repdigit(66) ➞ True
# is_repdigit(0) ➞ True
# is_repdigit(-11) ➞ False


def is_repdigit(digit:int):
    return len({num for num in str(digit)}) == 1

print(is_repdigit(66))