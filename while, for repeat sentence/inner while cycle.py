while True:
    print("1. atlikti skaičiaus daugybą\n"
          "2. išeiti")

    pasirinkimas = input()
    if pasirinkimas == "2":
        break

    if pasirinkimas == "1":
        # daugyba tęsis, kol nebus paspausta q
        while True:
            print("Įvesti skaičių daugybai iš 100 arba q - grįžti")
            ivestis = input()
            if ivestis == "q":
                break
            elif not ivestis.isdigit():
                print("Įvestas ne skaičius!!!")
                continue
            skaicius = int(ivestis) * 100
            print("Daugybos iš 100 rezultatas -", skaicius)