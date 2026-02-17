class Darbuotojas:
    def __init__(self, vardas, pavarde, pareigos):
        self.vardas = vardas
        self.pavarde = pavarde
        self.pareigos = pareigos

    def __iter__(self):
        return iter([self.vardas, self.pavarde, self.pareigos])

darbuotojas = Darbuotojas("Jonas", "Jonaitis", "Programuotojas")
for savybe in darbuotojas:
    print(savybe)