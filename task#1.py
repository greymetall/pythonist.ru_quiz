# -*- coding: utf-8 -*-

# Условие: Необходимо написать функцию, которая принимает строку и возвращает кол-во гласных внутри неё.
# Входная строка для примера "Pseudopseudohypoparathyroidism'
# Примечание: Глассными в английском являются (a, e, i, o, u)


def vowel_counter(str):
    counter = 0
    for alpha in str:
        if alpha in 'aeiou':
            counter += 1
    return counter


print(vowel_counter('Pseudopseudohypoparathyroidism'))
