houses_kaupiklis = []
while True:
    quit_choice = input("įveskite bet kokį simbolį kad išeiti Enter, tęsti įvedimą")
    if quit_choice:
        break

    year = int(input("Įveskite metus "))
    price = int(input("Įveskite kainą "))

    house_instance = House(price, year)
    houses_kaupiklis.append(house_instance)

    print("Spausdinam ką sukaupėm")
    for house in houses_kaupiklis:
        print(house)