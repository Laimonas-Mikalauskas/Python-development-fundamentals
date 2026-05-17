while True:
    ivestis = input("Įveskite float skaičių")
    try:
        float_skaicius = float(ivestis)
        print("Įvestis tinkama", float_skaicius)
        break
    except ValueError:
        print("Įvestis NETINKAMA, pakartokite!!!")
    finally:
        print("Manęs niekaip neatsikratysit - FINALLY komanda")

print("Programa tęsia darbą")