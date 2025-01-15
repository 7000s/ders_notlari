class ogrenci:
    #attribute
    okul_bilgisi = "Damyo"
    #constructer- yapıcı metod
    def __init__(self,ad,soyad,numara):
        self.ad = ad
        self.soyad = soyad
        self.numara = numara
    def bilgi(self):
        return f"{self.ad} {self.soyad} öğrecinin numarası : {self.numara} {self.okul_bilgisi}\'da öğrenci"
class ikincisinif(ogrenci):
    def __init__(self,ad,soyad,numara,brans):
        super().__init__(ad,soyad,numara)
        self.brans =brans


ogr1 = ogrenci("Berat", "Şahin",7429)
ogr2 = ogrenci("Halil İbo", "Şahinci",7052)
ogr3 = ikincisinif("Semih","Aydoğmuş",7042,"BT Bilişim")

print((ogr1.ad,ogr1.soyad,ogr1.numara))
print((ogr2.ad,ogr2.soyad,ogr2.numara))

print(ogr1.bilgi())
print(ogr2.bilgi())
print(ogr3.bilgi())