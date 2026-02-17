class Rytas:
    def __init__(self, name, city):
                
        self.title = name
        self.city = city

    def run(self):
        print(f"{self.title, self.city} runs to fast attack!")

    def throw(self):
        print(f"{self.title, self.city} throws the ball to the basket!")

    def attack(self):
        print(f"{self.title, self.city} attacks the opponent's basket!")

    def defense(self):
        print(f"{self.title, self.city} returns to defense.")

team = Rytas("Rytas", "Vilnius")

team.throw()
