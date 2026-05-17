listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# suma
suma = 0
for elem in listas:
    suma += elem  # kaupiame sumą
print("Suma yra:", suma)

# maksimalus skaičius
maksimalus = listas[0]
for elem in listas:
    if elem > maksimalus:
        maksimalus = elem  # randame maksimalų elementą
print("Maksimalus yra:", maksimalus)