class LKLTeam:
    def __init__(self, title, color):
        self.title = title
        self.color = color
    
class Rytas(LKLTeam):    
    def play(self):
        print(f"{self.title} Rytas plays the game!")
    
    def chant(self):
        print(f"{self.title}: fans are chanting Red-black!")

class Zalgiris(LKLTeam):
    def play(self):
        print(f"{self.title} Zalgiris plays the game!")
    
    def chant(self):
        print(f"{self.title}: fans are chanting Green-white!")

class Lietkabelis(LKLTeam):
    def play(self):
        print(f"{self.title} Lietkabelis plays the game!")
    
    def chant(self):
        print(f"{self.title}: fans are chanting Red-white!")

zalgiris = Zalgiris("Kauno Žalgiris", "green and white")
rytas = Rytas("Vilniaus Rytas", "red and black")
lietkabelis = Lietkabelis("Panevėžio Lietkabelis", "red and white")

def play_all_teams():
    zalgiris.play()
    rytas.play()
    lietkabelis.play()

def chant_all_teams():
    zalgiris.chant()
    rytas.chant()
    lietkabelis.chant()

play_all_teams()
chant_all_teams()