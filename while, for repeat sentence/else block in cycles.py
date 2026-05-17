for skaicius in range(1, 5):
    if skaicius % 2 == 0:
        print("Skaičius", skaicius, "yra lyginis")
    else:
        print("Skaičius", skaicius, "yra nelyginis")

print("-----")

for skaicius in range(1, 5):
    if skaicius % 2 == 0:
        print("Skaičius", skaicius, "yra lyginis")
else:
    print("Ciklas baigtas")