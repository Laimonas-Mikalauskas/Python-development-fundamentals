# Basic class - Player
class Player:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

# Inherited class  – Žalgiris
class ZalgirisPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

# Inherited class – Rytas
class RytasPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

# Inherited class – Lietkabelis
class LietkabelisPlayer(Player):
    def __init__(self, name, surname, age, position, team):
        super().__init__(name, surname, age)
        self.position = position
        self.team = team

zalgiris = ZalgirisPlayer("Edgaras", "Ulanovas", 32, "Puolėjas", "Kauno Žalgiris")
rytas = RytasPlayer("Margiris", "Normantas", 27, "Gynėjas", "Vilniaus Rytas")
lietkabelis = LietkabelisPlayer("Vytenis", "Lipkevičius", 36, "Light attacker of the side", "Panevėžio Lietkabelis" )

print(f"{rytas.name} {rytas.surname}, {rytas.age} m., {rytas.team}")
