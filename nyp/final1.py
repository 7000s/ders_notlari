#FONKSİYONLAR
def usler(uslu_sayi,us):
    return uslu_sayi ** us
print(usler(2,5)),

#Fonksiyonlar2
def üsAlma(taban,kuvvet): #3 4
    # sonuc = 1
    # for i in range(kuvvet):
    #     sonuc *= taban
    # return sonuc
    return  taban ** kuvvet

print(üsAlma(3,4))
print(üsAlma(2,5))

ogr_notlari = [72,40,42,85,90,100,30]

def dersKontrol(liste):
    for i in liste:
        if i>=50:
            print(f"Not : {i} Durum : Geçti")
        else:
            print(f"Not : {i} Durum : Kaldi")

dersKontrol(ogr_notlari)
dersKontrol([20,100,55])

#DOSYA OLUŞTURMA
ogr_listesi = ["Emrullah","Hamza","Semih","Efe"]

f = open('ogrenci.txt','a',encoding="utf-8")
for i in ogr_listesi:
    f.write(f"{i}\n")
f.close()
f = open("ogrenci.txt","r",encoding="utf-8")
yeni_list = []
for satir in f:
    yeni_list.append(satir)

print(yeni_list)

#CLASS
#Class
class Sekil:
    #atribute-yapıcı metot
    def __init__(self,kenar_sayisi,hacim,renk):
        self.kenar_sayisi = kenar_sayisi
        self.hacim = hacim
        self.renk = renk
    #metot
    def bilgi(self):
        print(f"Kenar Sayisi : {self.kenar_sayisi}")

    def renkBilgi(self):
        print(f"Renk : {self.renk}")
#alt sınıf
class Ucgen(Sekil):
    def __init__(self,kenar_sayisi,hacim,renk,tipi):
        super().__init__(kenar_sayisi,hacim,renk)
        self.tipi = tipi

s1 = Sekil(4,"10br","Mavi")
u1 = Ucgen(3,"5br","Sarı","ikizkenar")
print(s1.kenar_sayisi,s1.hacim)
s1.bilgi()
u1.bilgi()
s1.renkBilgi()
print(u1.kenar_sayisi,u1.hacim,u1.tipi)
u2 = Ucgen(3,"4br","Kırmızı","eşkenar")
u2.renkBilgi()


