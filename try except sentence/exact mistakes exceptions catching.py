ivestis1 = input("Įveskite sveiką skaičių")
ivestis2 = input("Įveskite daliklį")

try:
    skaicius = int(ivestis1)
    daliklis = int(ivestis2)
    res = skaicius / daliklis
except ValueError:
    print("Mes crashinom su ValueError")
    print("Paleiskite programą išnaujo ir ivestis padarykit kad tai būtų sveikas skaičius")
except ZeroDivisionError:
    print("Mes crashinom su ZeroDivisionError")
    print("Pakeiskite daliklį iš 0 į kitą")

print("Programa tęsia darbą")