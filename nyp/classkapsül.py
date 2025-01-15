class Personel:
    def __init__(self,ad,maas):
        self.ad = ad
        self.__maas = maas
    def get_maas(self): #kontrollü okuma
        return self.__maas

    def set_maas(self,yeni_maas): #kontrollü değişim
        self.__maas = yeni_maas
p1 = Personel("Sertaç",84000)
p1.ad = "Enes"
# p1.maas = 22000
p1.set_maas(42000)
print(p1.ad)
print(p1.get_maas())
