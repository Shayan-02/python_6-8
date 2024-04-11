# class Person:
#     def __init__(self,person_name, person_age):
#         self.person_name = person_name
#         self.person_age = person_age
#     def __str__(self):
#         return f"person name is {self.person_name} and person age is {self.person_age}"
#
# p1 = Person("ali", 25)
# print(p1.__str__())
# print(p1.__repr__())
# print(p1)
# print(str(p1))

import calendar

# year = int(input("Year: "))
# month = int(input("Month: "))

print(calendar.TextCalendar().formatmonth(2022, 12))
