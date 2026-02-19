def player_info(func):
    def info(name, score, balls, *args, **kwargs):
        print("Houston Rockets team player statistics")
        func(name, score, balls, *args, **kwargs)
    return info

def uniform_info(func):
    def info(*args, **kwargs):
        print("Houston Rockets team colors")
        func(*args, **kwargs)
    return info

@player_info
@uniform_info
def show_info(name, points, balls, colors, logo, city):
    print(f"{name} scored {points} points and took {balls} balls. Team colors: {colors}, Logo: {logo}, City: {city}")

show_info("Donatas Motiejunas", 24, 6, "blue, red", "hawk", "Houston")






