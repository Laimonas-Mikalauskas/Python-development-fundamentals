class School:
    city = 'Vilnius'

    def __init__(self, name, student_count):
        self.name = name
        self.student_count = student_count

school1 = School('Vilniaus gimnazija', 450)
school2 = School('Kauno gimnazija', 320)

print(school1.name, school1.student_count, school1.city)
print(school2.name, school2.student_count, school2.city)

schools = [
    School('Klaipedos gimnazija', 450),
    School('Akmenes gimnazija', 320)
]

for school in schools:
    print(school.name, school.student_count, school.city)

print(School.city)

print(school1)
print(f'Name: {school1.name}, student count: {school1.student_count}')




