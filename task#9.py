# -*- coding: utf-8 -*-

# Задание: Создайте атрибуты fullname и email в классе Employee.
# При заданных имени и фамилии человека:
# - сформируйте fullname, просто соединяя имя с фимилией через пробел,
# - сформируйте email, соединяя имя и фамилию через точку и добавляя
# @company.com (http://%5C@company.com/) в конце.
# Весь email должен быть  в нижнем регистре.

# Примеры:
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")

# emp_1.fullname ➞ "John Smith"
# emp_2.email ➞ "mary.sue@company.com"
# emp_3.firstname ➞ "Antony"

# Примечание: атрибуты firstname и lastname уже есть в готовом виде.


class Employee:
    """Employees personal data class"""
    def __init__(self, firstname:str, lastname:str):
        self.firstname, self.lastname = firstname, lastname
        self.fullname = f'{firstname} {lastname}'
        self.email = f'{firstname.lower()}.{lastname.lower()}@company.com'

        
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(f"{'-':-^53}")
print(f"|{'name':^20}|{'email':^30}|")
print(f"{'-':-^53}")
print(f'|{emp_1.fullname:^20}|{emp_1.email:^30}|')
print(f'|{emp_2.fullname:^20}|{emp_2.email:^30}|')
print(f'|{emp_3.fullname:^20}|{emp_3.email:^30}|')
print(f"{'-':-^53}")
# print(emp_1.fullname)
# print(emp_1.email)
# print(emp_2.fullname)
# print(emp_2.email)
# print(emp_3.fullname)
# print(emp_3.email)
# print(emp_3.firstname)