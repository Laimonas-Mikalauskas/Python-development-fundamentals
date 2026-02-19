# Example 4
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

person = {
    'name': 'Jonas',
    'country': 'LT',
    'birth_date': '1990',
    'books': [
        Book('Title1', 'Author1'),
        Book('Title2', 'Author2'),
        Book('Title3', 'Author3'),
    ]
}

for key, value in person.items():
    if isinstance(value, list):
        print(f'{key}:')
        line_number = 1
        for book in value:
            print(f'{line_number}. Title: {book.title}, Author: {book.author}')
            line_number += 1
    else:
        print(f'{key}: {value}')

# Example 3
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
# students = [
#     Student('Jonas', 10),
#     Student('Darius', 9),
#     Student('Ona', 8)
# ]
#
# for student in students:
#     print(f'name: {student.name}, grade: {student.grade}')


# Example 2
# class House:
#     country = 'LT'
#
#     def __init__(self, price, year):
#         self.price = price
#         self.year = year
#
# # print(House.country)
#
# house_instance_1 = House(10000, 1990)
#
# print(house_instance_1.country)
# print(house_instance_1.price)
# print(type(house_instance_1))
#
#
# house_instance_2 = House(12000, 1920)
#
# print(house_instance_2.country)
# print(house_instance_2.price)
# print(house_instance_2.year)


# Example 1
# class House:
#     country = 'LT'
# print(House.country)
#
# class Car:
#     wheels = 4
# print(Car.wheels)
#
# class Currency:
#     symbol = '$'
# print(Currency.symbol)
