# -*- coding: utf-8 -*-

# Задание: Создайте функцию, которая принимает одну строку и
# возвращает другую, в которой каждая буква исходной строки
# повторяется дважды.

# Примечание: Все тестовые случаи содержат валидные строки.
# Не переживайте о пробелах, специальных символах или цифрах.
# Все эти символы валидны.

# Примеры: 
# double_char("String") ➞ "SSttrriinngg"
# double_char("Hello World!") ➞ "HHeelllloo  WWoorrlldd!!"
# double_char("1234!_ ") ➞ "11223344!!__  "


def double_char(txt:str):
    return ''.join((map(lambda x: x*2, txt)))

print(double_char('Hello World!'))