# Example 3

class Serveris:
    def __init__(self):
        self._slaptas_raktas = 'ABC123'

    def autentifikuoti(self, raktas):
        return raktas == self._slaptas_raktas


serv = Serveris()
user_input = input()

auth = serv.autentifikuoti(user_input)

if not auth:
    print('Neteisingas slaptazodis')

# Example 2
# class BankOperations:
#     def papidyti(self, suma):
#         self._balansas += suma
#
#     def balansas(self):
#         return self._balansas
#
#
# class BankoSaskaita(BankOperations):
#     def __init__(self):
#         self._balansas = 0
#
# s = BankoSaskaita()
# s.papidyti(100)
# s.papidyti(100)
# s.papidyti(-100)
# print(s.balansas())


# Example 1
# class Asmuo:
#     def __init__(self, name):
#         self._name = name
#
#     def rodyti_varda(self):
#         print(self._name)
#
# class Darbuotojas(Asmuo):
#     def rodyti_info(self):
#         print(self._name)
#
#
# a = Asmuo('Jonas')
# print(a._name)
# a.rodyti_varda()
