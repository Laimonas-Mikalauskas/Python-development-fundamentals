from datetime import datetime

# Example 3
class House:
    country = 'LT'

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def __str__(self):
        return f'Namas {self.year} pastatymo, kaina - {self.price}, amzius - {self.get_age()}'

    def get_age(self):
        now = datetime.today()
        current_year = now.year
        return current_year - self.year

house1 = House(200000, year=2024)

print(house1)

# Example 2
# class Phone:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def with_tax(self):
#         return round(self.price * 1.21)
#
# phones = [
#     Phone('Iphone 16 pro max', 1500),
#     Phone('Galaxy s25 Ultra', 1300),
# ]
#
# for phone in phones:
#     print(f'Name: {phone.name}, price: {phone.price}, price with tax: {phone.with_tax()}')

# Example 1
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def is_passing(self):
#         return self.grade >= 5
#         # if self.grade >= 5:
#         #     return True
#         # return False
#
# student1 = Student('Jonas', 10)
# student2 = Student('Ona', 4)
#
# print(f'Name: {student1.name}, grade: {student1.grade}, is_passing: {student1.is_passing()}')
# print(f'Name: {student2.name}, grade: {student2.grade}, is_passing: {student2.is_passing()}')
#
