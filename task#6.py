# -*- coding: utf-8 -*-

# Условие: Напишите функцию, которая будет принимать список из
# двух чисел и определять, равны ли суммы цифр в этих двух числах.

# Примеры: 
# is_equal([105, 42]) ➞ True
# is_equal([21, 35]) ➞ False
# is_equal([0, 0]) ➞ True


is_equal = lambda elems: len({sum(int(num) for num in str(elem)) for elem in elems})<2


print(is_equal([105, 42]))