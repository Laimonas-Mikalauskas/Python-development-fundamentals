listas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
flag5 = False
flag3 = False

for elem in listas:
    print(elem)
    if elem % 5 == 0:
        flag5 = True
    if elem % 3 == 0:
        flag3 = True

    if flag5 and flag3:
        break

if flag5:
    print("Liste yra elementas kuris dalinasi iš 5")
if flag3:
    print("Liste yra elementas kuris dalinasi iš 3")