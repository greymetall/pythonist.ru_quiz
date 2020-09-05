# -*- coding: utf-8 -*-

# Условие: Напишите функцию, которая находит наибольшее четное число в списке.
# Верните  -1 если ничего не найдено.
# Использовать встроенные функции max() и sorted() - запрещено

# Пример:  largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10

# Список для задачи: [0, 19, 18973623].


def largest_even(test_list):
    max_dct = {}
    evens = [elem for elem in test_list if not elem % 2]
    max_dct = {'max_even':even for even in evens if even > max_dct.get('max_even', -1)}
    return max_dct.get('max_even', -1)

    
print(largest_even([0, 19, 18973623]))