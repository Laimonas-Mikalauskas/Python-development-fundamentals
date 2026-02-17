def skaiciuok_iki(max_reiksme):
    skaicius = 0
    while skaicius < max_reiksme:
        yield skaicius
        skaicius += 1

for numeris in skaiciuok_iki(5):
    print(numeris)