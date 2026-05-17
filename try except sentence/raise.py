def sumuok_int_skaicius(sk1: int, sk2: int) -> int:
    if not (type(sk1) is int and type(sk2) is int):
        raise ValueError  # iššaukiame klaidą, jei argumentai nėra sveiki skaičiai
    return sk1 + sk2

res = sumuok_int_skaicius(4, 5)
print(res)