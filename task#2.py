# -*- coding: utf-8 -*-

# Условие: Необходимо написать функцию, которая вернёт сумму всех элементов списка умноженных на свой индекс. Для пустого списка возвращаем 0. 
# Пример: index_multiplier([1, 2, 3, 4, 5]) ➞ 40. 


index_multiplier = lambda lst: sum(i*elem for i, elem in enumerate(lst))
index_multiplier([1, 2, 3, 4, 5])