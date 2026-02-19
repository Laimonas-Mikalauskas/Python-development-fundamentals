def player_info(func):
    def info(name, points, rebounds):
        print("Rytas's player statistics")
        func(name, points, rebounds)
    return info

@player_info
def player_statistics(name, points, rebounds):
    print(f"{name} scored {points} points and got {rebounds} rebounds")

player_statistics("Margiris Normantas", 18, 6)