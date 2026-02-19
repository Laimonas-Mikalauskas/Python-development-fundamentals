for house in houses:
    print(f"sena kaina: {house.price}")
    house.price = round(house.price * 1.21)
    print(f"nauja kaina: {house.price}")

print(house1)