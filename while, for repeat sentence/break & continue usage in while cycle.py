while True:
    print("kartojimo pradžia")
    print("1. šis meniu punktas nedaro nieko\n"
          "2. išeiti iš kartojimo bloko\n"
          "3. vėl parodyti meniu")

    pasirinkimas = input()
    if pasirinkimas == "2":
        break
    elif pasirinkimas == "3":
        continue
    else:
        print("nieko nebuvo pasirinkta")
    print("kartojimo pabaiga")