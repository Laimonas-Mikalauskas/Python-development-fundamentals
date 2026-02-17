# Example 3
class BankoSaskaita:
    def __init__(self):
        self.__balansas = 0

    def papildyti(self, suma):
        self.__balansas += suma

    def balansas(self):
        print(self.__balansas)


acc = BankoSaskaita()
acc.papildyti(100)
acc.balansas()

# Example 2
# class Asmuo:
#     def __init__(self, vardas):
#         self.__vardas = vardas
#
#     def rodyti_varda(self):
#         print(self.__vardas)
#
# class Vaikas(Asmuo):
#     def rodyti_info(self):
#         try:
#             print(self.__vardas)
#         except:
#             print('Nepasiekiamas privatus atributas')
#
# jonas = Vaikas('Jonas')
# jonas.rodyti_info()



# Example 1
# class Asmuo:
#     def __init__(self, vardas):
#         self.__vardas = vardas
#
#     def rodyti_varda(self):
#         print(self.__vardas)
#
#
# jonas = Asmuo('Jonas')
# jonas.rodyti_varda()
# print(jonas.__vardas)
