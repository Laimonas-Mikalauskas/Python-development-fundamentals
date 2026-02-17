def apversti_teksta(tekstas):
    return tekstas[::-1]

def apversti_sakini(tekstas):
    return " ".join(tekstas.split()[::-1])

print(apversti_teksta("ABC"))
print(apversti_sakini("Labas Pasauli Dabar!!!"))

def i_didziasias(tekstas, funkcija=None):
    if funkcija:
        tekstas = funkcija(tekstas)
    return tekstas.upper()

print(i_didziasias("abc", funkcija=apversti_teksta))
print(i_didziasias("Labas Pasauli Dabar!!!", funkcija=apversti_sakini))