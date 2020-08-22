# -*- coding: utf-8 -*-

# Условие: Используя list comprehensions, напишите функцию, которая выводит все четные числа до числа, которое передано функции

# Пример: find_even_nums(8) ➞ [2, 4, 6, 8]
#         find_even_nums(4) ➞ [2, 4].
# Если нет четных чисел - возвращаем пустой список.


find_even_nums = lambda n: [num for num in range(1, n+1) if not num%2] 
print(find_even_nums(8))