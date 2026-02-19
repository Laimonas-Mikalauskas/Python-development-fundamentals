class School:
    city = "Vilnius"

    def __init__(self, name, student_count):
        self.name = name
        self.student_count = student_count

    def is_big_school(self):
        # return self.student_count > 500
        if self.student_count > 500:
            return True
        return False

    def __str__(self):
        return f"{self.name} mokykla, {self.student_count} mokinių, miestas: {self.city}"


school1 = School("Vilniaus gimnazija", 450)
school2 = School("Kauno progimnazija", 320)

print("Užduotis 5:")
school3 = School("Šiaulių licejus", 700)
print(school1.is_big_school())
print(school3.is_big_school())
print()

print("Užduotis 6:")
schools = [
    School("Vilniaus mokykla", 300),
    School("Kauno gimnazija", 520),
    School("Klaipėdos progimnazija", 499),
    School("Panevėžio licejus", 800)
]

for s in schools:
    status = "DIDELĖ mokykla" if s.is_big_school() else "NĖRA didelė mokykla"
    print(f"{s.name} – {s.student_count} mokinių – {status}")
print()

print("Užduotis 7:")
print(school1)
print(school2)
print(school3)

