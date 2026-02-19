class House:
    country = "LT"

    def __init__(self, price, year):
        self.price = price
        self.year = year

    def get_age(self):
        now = datetime.datetime.today()
        current_year = now.year
        return current_year - self.year

    def __str__(self):
        return f"Namas {self.year} pastatymo, kaina - {self.price}, amžius - {self.get_age()}"