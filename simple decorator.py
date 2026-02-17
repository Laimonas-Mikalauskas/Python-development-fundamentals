def registratorius(funkcija):
    def apvalkalas(argumentas):
        rezultatas = funkcija(argumentas)
        if rezultatas % 2 == 0:
            print(f"{rezultatas} yra lyginis")
        else:
            print(f"{rezultatas} yra nelyginis")
        return rezultatas
    return apvalkalas

@registratorius
def kvadratu(skaicius):
    return skaicius ** 2

print(kvadratu(8))