# Example 2
students = []

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def is_passing(self):
        return self.grade >= 5

    def __str__(self):
        return f'Studentas: {self.name}, pazymis {self.grade}'

def print_all_students():
    if not students:
        print('Studentu kol kas nera!')
    for student in students:
        print(student)

def add_student():
    student_name = input('Studento vardas: ')
    student_grade = int(input('Studento pazymys: '))
    students.append(Student(student_name, student_grade))

def get_student_info_by_name():
    student_name = input('Studento vardas: ')
    for student in students:
        if student.name == student_name:
            print(student)

def delete_student_by_name():
    student_name = input('Studento vardas: ')
    i = 0
    for student in students:
        if student.name == student_name:
            del students[i]
        i += 1

print('Sveiki, atvyke!')
while True:
    print('')
    print('Meniu:')
    print('1. Gauti visu studentu sarasa')
    print('2. Prideti studenta')
    print('3. Gauti studento informacija pagal varda')
    print('4. Istrinti studenta')
    print('5. Iseiti')
    print('')

    user_input = int(input('Pasirinkimas: '))

    if user_input == 1:
        print_all_students()
    if user_input == 2:
        add_student()
    if user_input == 3:
        get_student_info_by_name()
    if user_input == 4:
        delete_student_by_name()
    if user_input == 5:
        break



#  Example 1
# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#
#     def is_passing(self):
#         return self.grade >= 5
#
#     def __str__(self):
#         return f'Studentas: {self.name}, pazymis {self.grade}'
#
#
# student1 = Student('Jonas', 10)
# # print(student1)
# #
# # student1.name = 'Marius'
# # student1.grade = 9
# # print(student1)
#
# students = [
#     Student('Jonas', 5),
#     Student('Ona', 10),
#     Student('Ieva', 8),
#     Student('Darius', 10),
#     Student('John', 6),
# ]
#
# for student in students:
#     if student.grade < 10:
#         student.grade += 1
#     print(student)
#
# student1.surname = 'Jonaitis'
#
# print(student1.surname)
