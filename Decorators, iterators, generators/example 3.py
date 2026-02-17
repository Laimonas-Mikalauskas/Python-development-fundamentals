# Example 2

class Kvadratas:
    def __init__(self, krastine):
        self.__krastine = krastine

    @property
    def krastine(self):
        return self.__krastine

    @krastine.setter
    def krastine(self, nauja_krastine):
        if nauja_krastine > 0:
            self.__krastine = nauja_krastine
        else:
            print('Krastine turi buti teigiama')


k = Kvadratas(5)

k.krastine = 20

print(k.krastine)



# Example 1
# class Kvadratas:
#     def __init__(self, krastine):
#         self._krastine = krastine
#
#     @property
#     def plotas(self):
#         return self._krastine ** 2
#
# k = Kvadratas(4)
# k._krastine = 20
# print(     k.plotas      )
