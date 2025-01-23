class araba:
    def __init__(self,marka,model,yas):
        self.marka = marka
        self.model = model
        self.yas = yas
    def bilgi(self):
        print(f"arabanın markası : {self.marka} \nmodeli : {self.model} \nyasi : {self.yas}")
class deger(araba):
    def __init__(self,marka,model,yas,fiyat):
        super().__init__(marka,model,yas)
        self.fiyat = fiyat
    def fiyati(self):
        print(f"arabanın fiyatı : {self.fiyat}")


a1 = araba("toyota","verso",15) #özellik değerleri
a2 = deger("mercedes","a180",5,900000)
print(a1.marka,a1.model,a1.yas,a2.marka,a2.model,a2.yas,a2.fiyat) #fonksiyonsuz çağırma
a1.bilgi() #fonksiyondan çağırma
a2.bilgi()
a2.fiyati()