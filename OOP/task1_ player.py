def player_info(func):
    def info(*args, **kwargs):
        print("Vilniaus Rytas team player statistics")
        func(*args, **kwargs)
    return info

def uniform_info(func):
    def uniform(*args, **kwargs):
        print("Vilniaus Rytas team attributes")
        func(*args, **kwargs)
    return uniform

@player_info
@uniform_info
def show_info(name, points, balls, colors, logo, city):
    print(f"{name} score {points} points and returns {balls} balls and team {colors} isa black white red. Logo is {logo} from city {city}")

show_info("Margiris Normantas", 16, 6, "black white red", "Wolf", "Vilnius")