# -*- coding: utf-8 -*-

# Условие: Напишите программу используя re, которая конвертирует дату из формата yyyy-mm-dd format в  dd-mm-yyyy формат

import re

def data_reformer(input_date):
    parse_date = re.findall(r"\b([0-9]{4})[-/:]([0-9]{2})[-/:]([0-9]{2})\b", input_date)
    if parse_date:
        is_true_month = parse_date[0][1] in [f'{month:02}' for month in range(1,13)]
        is_true_day = parse_date[0][2] in [f'{day:02}' for day in range(1,32)]
        conditions = all([is_true_month, is_true_day])
    else:
        conditions = False
    if conditions:
        output_date = '-'.join(reversed(parse_date[0]))
        return output_date
    else:
        return "дата некорректна"


input_date = '2020-08-30'
print(data_reformer(input_date))