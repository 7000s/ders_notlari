ip # def pozitifkontrol(n):
#     if n > 0:
#         print("Pozitif")
#     elif n<0:
#         print('Negatif')
#     else:
#         print("Sayı 0 a esittir.")
# pozitifkontrol(56)
# pozitifkontrol(-6)
#
# def mesajyaz(s,mesaj):
#         for i in range(s):
#             print(mesaj)
# mesajyaz(3,"Berat")
#
# def fakt(sayi):
#     f = 1
#     for i in range(2,sayi+1):
#         f = f * i
#     return f
#
# # s1 = fakt(5)
# # s2 = fakt(4)
# # top = s1 + s2
# print(fakt(3)+ fakt(4))
#
#
# a = lambda x,y: x + y
# b = lambda z: print(z)
# print(a(3,5))
# b('Emirhan')
# b(8)

# def ushesaplama(taban,kuvvet):
#     sonuc = 1
#     for i in range(kuvvet):
#         sonuc = sonuc * taban
#     return sonuc
#
# print(ushesaplama(3,4))
# print(ushesaplama(2,8))
# a = ushesaplama(5,3)
# print(a)
# def topla(*params):
#     print(sum(params))
#
# def yazdir(*params):
#     for x in params:
#         print(x)
#
# liste = ['Ahmet',34,'deniz']
# yazdir(3,'Enes','BT',"Damyo",7000)
# topla(3,2,72)
# yazdir(liste)

# def bilgi(a,b,d,*pr):
#     print(a)
#     print(b)
#     print(d)
#     print(pr)
#
# bilgi('dogukan',3,5,8,7,9,58,3)
#
# dc = {
#     "ad" : "emirhan",
#     "soyad" : 'celik',
#     'ogr_no' : 7135
# }
# def sozlukverisi(**abc):
#     print(abc)
# sozlukverisi(ad = "halil ibo",soyad = 'sahinci',ogr_no = 7052)








# import random
# notlar = []
# for x in range(13):
#     notlar.append(random.randint(50,100))

# print(notlar)
# ogr_list = ["Abdullah","Semih","Enes","İbrahim","Doğukan","Hamza","Berat","Emrullah","M.Emin","Efe"]
# sonuc= random.choice(ogr_list)
# sonuc=random.sample(ogr_list,2)

class Personel:
    def __init__(self,ad,maas):
        self.ad = ad
        self.__maas = maas
    def get_maas(self):
        return self.__maas
p1 = Personel("ali",57000)

p1.ad = "ping 
print(p1.ad)
print(p1.get_maas())












# #import math
# from math import *
# #print(help(math))
# sayi = 16
# sonuc = sqrt(sayi)
# sonuc = pow(5,3)
# print(sonuc)
import random

# print(help(random))
sonuc = random.random()
sonuc = random.randint(5,42)

notlar = []
for x in range(13):
    notlar.append(random.randint(50,100))

print(notlar)
ogr_list = ["Abdullah","Semih","Enes","İbrahim","Doğukan","Hamza","Berat","Emrullah","M.Emin","Efe"]
sonuc = random.choice(ogr_list)
#random.shuffle(ogr_list)
sonuc = random.sample(ogr_list,5)
sonuc = random.choices(ogr_list,weights=[10,1,1,1,1,1,1,1,1,1],k=10)
sonuc = random.randrange(5,40,5)
print(sonuc)











# open('dosyaadi',"mode")
# x = dosya oluşturur , eğer varsa hata döndürür.
# w = yaz, yoksa dosya oluşturur eğer varsa dosyayı yeniden oluşturur.
# a = ekle, yoksa dosya oluşturur eğer dosya varsa üzerine ekler
# r = okuma yapar eğer dosya hata döndürür. Varsayılandır
# f = open("test1.txt","x") #x mode
# f = open("test.txt","w")
# f = open("test.txt","a")
# f.write("Berat")
# f = open("test.txt")
# print(f.read())
# f.write("\nAbdullah")
# print(f.read())
# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines()[2])
# for satir in f:
#     print(satir,end="") #end komutu aralarındaki boslugu belirler
# ogrenci = open("ogrenci.txt","a",encoding="utf-8")
# # for i in range(3):
# #     ogrenci_bilgi = input(f"\n{i+1}.ogrencinin bilgisini gir :")
# #     ogrenci.writelines(ogrenci_bilgi)
# ogrenci = open("ogrenci.txt","r",encoding="utf-8")
# ogr_lst = []
# for x in ogrenci:
#     ad = x.split(' ')[0]
#     soyad = x.split(' ')[1]
#     numara = x.split(' ')[-1]
#     ogr_lst.append({"ad": ad,"soyad":soyad,"ogr_no":numara})
# print(ogr_lst)
from http.cookiejar import deepvalues
from secrets import choice

from encodings.punycode import adapt

# ogr_list = ["Semih","Halil İbo","İbrahim","Sertaç","M.Emin"]
# ogrenci = open("ogr_list.txt","r+",encoding="utf-8")
# ogrenci.writelines(ogr_list)
# for i in ogr_list:
#     ogrenci.write(f"{i}\n")
# ogrenci.close()
# icerik = ogrenci.readline()
# print(icerik)
# icerik2 = ogrenci.readline()
# print(icerik2)
# print(ogrenci.tell())
# ogrenci.seek(3)
# icerik2 = ogrenci.readline()
# print(icerik2)
# icerik = ogrenci.read()
# print(ogrenci.tell())
# ogrenci.seek(3)
# print(ogrenci.read())
# print(ogrenci.tell())
# icerik = ogrenci.read()
# lst = icerik.split(',')
# print(lst)
# abc = "Semih,Halil İbo,İbrahim,Sertaç,M.Emin"
# print(abc.split(','))
# yeni_liste = []
# with open("ogr_list.txt","r+",encoding="utf") as ogrenci:
#     for ogr in ogrenci:
#         yeni_liste.append(ogr)
#     # icerik = ogrenci.read()
#     # yeni_liste = icerik.split(',')
#
# print(yeni_liste)
# for i in range(len(yeni_liste)):
#     yeni_liste[i] = {
#         yeni_liste[i].split(',')[0].split(':')[0] : yeni_liste[i].split(',')[0].split(':')[1],
#         yeni_liste[i].split(',')[1].split(':')[0]: yeni_liste[i].split(',')[1].split(':')[1],
#         yeni_liste[i].split(',')[2].split(':')[0]: yeni_liste[i].split(',')[2].split(':')[1]
#     }
#     print(i)
# print(yeni_liste[2])

# class Ogrenci :
#     # attribute
#     okul_bilgisi = "Damyo"
#     #constructur - yapıcı metot
#     def __init__(self,ad,soyad,numara):
#         self.ad = ad
#         self.soyad = soyad
#         self.numara = numara
#
#     def bilgi(self):
#
#
#
#         return f"{self.ad} {self.soyad} ogrencisinin numarasi  :  {self.numara} . {self.okul_bilgisi} \' da ogrenci olarak kayıtlıdır :"
# ogr1 = Ogrenci("Berat","Şahin","7429")
# ogr2 = Ogrenci("Halil İbo","Şahinci","7052")
#
#
# print(ogr1.ad ,ogr1.soyad ,ogr1.numara)
# print(ogr2.ad ,ogr2.soyad ,ogr2.numara)
#
# print(ogr1.bilgi())
#
# class Personel:
#     def __init__(self, ad, dogum_yili, maas):
#         self.ad = ad
#         self.dogum_yili = dogum_yili
#         self.maas = maas
#
#
#     def yashesapla(self) :
#       return f"{self.ad} personelinin yasi  : {2025 - self.dogum_yili}"
# class Mudur(Personel):
#     def __init__(self,ad,dogum_yili,maas,arac_sayisi,ek_maas):
#         super().__init__(ad,dogum_yili,maas)
#         self.arac_sayisi = arac_sayisi
#         self.ek_maas = ek_maas
#     def AracDurumu(self):
#         return self.arac_sayisi
# p1 = Personel('Enes','2003',45000)
# p2  = Personel('Dogukan', '2004', 4000)
# m1 = Mudur ('Emrullah',2001,8700,1,24500)
#


#classsssssssssssssssssssssssssssssssssssssssssssssssssssssssssss
# # class Ogrenci:
# #     #attribute
# #     okul_bilgisi = "Damyo"
# #     #constructur-Yapıcı Metot
# #     def __init__(self,ad,soyad,numara):
# #         self.ad = ad
# #         self.soyad = soyad
# #         self.numara = numara
# #     def bilgi(self):
# #         return f"{self.ad} {self.soyad} öğrencisinin numarası : {self.numara}. {self.okul_bilgisi}\'da öğrenci olarak kayıtlıdır."
# #
# # class IkinciSinif(Ogrenci):
# #     def __init__(self,ad,soyad,numara,brans):
# #         super().__init__(ad,soyad,numara)
# #         self.brans = brans
# #     def tabur(self):
# #         return f"Ikinci sınıf öğrencisi {self.ad} {self.soyad} tabura katılmaz"
# #
# #
# # ogr1 = Ogrenci("Berat","Şahin",7429)
# # ogr2 = Ogrenci("Halil İbo","Şahinci",7052)
# # ogr3 = IkinciSinif("Semih","Aydoğmuş",7042,"BT Bilişim")
# # ogr4 = IkinciSinif("Abdullah","Çubuk",7099,"Y/S")
# # print(ogr1.ad,ogr1.soyad,ogr1.numara)
# # print(ogr2.ad,ogr2.soyad,ogr2.numara)
# # print(ogr1.bilgi())
# # print(ogr2.bilgi())
# # print(ogr3.bilgi())
# # print(ogr3.tabur())
# # print(ogr4.tabur())
# #
# # o1 = {
# #     "ad" : "SertaÇ"
# # }
# # o2 = {
# #     "adi" :
# # }
# class Personel:
#
#     def __init__(self,ad,dogum_yili,maas):
#         self.ad = ad
#         self.dogum_yili = dogum_yili
#         self.maas = maas
#
#     def yashesapla(self):
#         return f"{self.ad} personelinin yasi : {2025 - self.dogum_yili}"
# class Mudur(Personel):
#     def __init__(self,ad,dogum_yili,maas,arac_sayisi,ek_maas):
#         super().__init__(ad,dogum_yili,maas)
#         self.arac_sayisi = arac_sayisi
#         self.ek_maas = ek_maas
#     def AracDurumu(self):
#         return self.arac_sayisi
# p1 = Personel("Enes",2003,45000)
# p2 = Personel("Dogukaan",2004,4000)
# m1 = Mudur("Emrullah",2002,8000,2,15000)
# print(p1.yashesapla())
# print(m1.yashesapla())
# print(m1.AracDurumu())
# print(p1.AracDurumu())
#__init__
# class Araba:
#     #attribute
#     def __init__(self,marka,model,km,uretim_yili):
#         self.marka = marka
#         self.model = model
#         self.km = km
#         self.uretim_yili = uretim_yili
#
#     #method
#     def trafikteBulunmaYasi(self):
#         return 2025 - self.uretim_yili
#     # def bakimKontrol(self):
#     #     bakim_sayisi = self.km // 10000
#     #     son_bakim_km = 10000*bakim_sayisi
#     #     if self.km - son_bakim_km > 9999:
#     #         print("Bakim zamani gelmiştir")
#     #     else:
#     #         print(f"Son bakim zamani : {son_bakim_km}")
#
# a1 = Araba("Seat","Ibiza",207150,2013)
# a2 = Araba("Honda","Civic",42000,2021)
#
# print(a1.marka,a1.model,a1.km,a1.uretim_yili)
# print(f"{a2.marka} {a2.model} {a2.km} {a2.uretim_yili}")
# print(a1.__dict__)
#
# print(a1.trafikteBulunmaYasi())
# print(a2.trafikteBulunmaYasi())
# #


# ***********Soru1*****************
# Berat ŞAHİN 7420
# Enes DURSUNOĞLU 7342
# Halilİbrahim ŞAHİNCİ 7052
# Hamza SAVAŞ 7044
# ogrenci.txt dosya içerisinde öğrenci bilgileri mevcuttur. Bu bilgileri ogrenci_listesi(veri türü = list)
# içerisine aktararak ogrenci_listesi'ni' ekrana yazdırınız.
# ogrenci = open("ogrenci.txt","+r",encoding="utf-8")
# ogrenci_listesi = []
# for ogr in ogrenci:
#     print(ogr, end="")
#     ogrenci_listesi.append(ogr)
#
# print(ogrenci_listesi)

# ***********Soru2*****************

# Klavyeden 3 ogrenci bilgisini(ad,soyad,numara) alarak bunu ogrenci_listesi.txt dosyasına yazdırınız.
# ogrenci_listesi.txt dosyası aynı klasör içerisinde bulunmamaktadır.

# ogrenci = open("ogrenci_listesi.txt","a",encoding="utf-8")
#
# for i in range(2):
#     ad = input("Ogrenci Adinin Gir :")
#     ogrenci.write(ad +" ")
#     soyad = input("Ogrenci Soyadini Gir :")
#     ogrenci.write(soyad + " ")
#     numara = input("Ogrenci Numarasini Gir :")
#     ogrenci.write(numara + "\n")

# ***********Soru3*****************

# class Personel:
#     def __init__(self, ad, dogum_yili, maas):
#         self.ad = ad
#         self.dogum_yili = dogum_yili
#         self.maas = maas
#
#
#     def yashesapla(self) :
#       return f"{self.ad} personelinin yasi  : {2025 - self.dogum_yili}"
# class Mudur(Personel):
#     def __init__(self,ad,dogum_yili,maas,arac_sayisi,ek_maas):
#         super().__init__(ad,dogum_yili,maas)
#         self.arac_sayisi = arac_sayisi
#         self.ek_maas = ek_maas
#     def AracDurumu(self):
#         return self.arac_sayisi

# ***********Soru4*****************

# sayi = int(input("Sayi Gir : "))
# liste = [85,75,42,96,30,24,65]
#
# def dersKontrol(*liste):
#     for i in liste[0]:
#         if i>=50:
#             print("Geçti")
#         else:
#             print("Kaldi")
#
# dersKontrol(liste)

# ***********Soru5*****************

# from random import random, randrange
#
# sifre = []
# for i in range(12):
#     rastgele_karakter = chr(randrange(55,125))
#     sifre.append(rastgele_karakter)
#
# print(''.join(sifre))

# ***********Soru6*****************

# import random
# notlar = []
# for x in range(13):
#     notlar.append(random.randint(50,100))
#
# print(notlar)
ogr_list = ["A","B","C","D","E","F","G","H","I","İ","K","L"]
# sonuc= random.choice(ogr_list)
# sonuc=random.sample(ogr_list,2)

class Sekil:
    def __init__(self, renk="mavi", konum=(0, 0)):
        self.__renk = renk
        self.__konum = konum

    def hareket_ettir(self, x, y):
        self.konum = (self.konum[0] + x, self.konum[1] + y)

    def bilgileri_goster(self):
        print(f"Renk: {self.renk}, Konum: {self.konum}")

    def getter(self):
        return  self.__renk
    def setter(self,renk):
        self.__renk = renk

class Kare(Sekil):
    def __init__(self, kenar_uzunlugu, renk="mavi", konum=(0, 0)):
        super().__init__(renk, konum)
        self.kenar_uzunlugu = kenar_uzunlugu

    def alan(self):
        return self.kenar_uzunlugu ** 2

class Daire(Sekil):
    def __init__(self, yaricap, renk="mavi", konum=(0, 0)):
        super().__init__(renk, konum)
        self.yaricap = yaricap

    def cevre(self):
        return 2 * 3.14 * self.yaricap

s1 = Kare(3,"siyah",(0,45))
s1.kenar_uzunlugu = 5
print(s1.setter("mavi"))
# from random import *
# shuffle(ogr_list)
#
# sonuc = dict()
# torba1 = list.copy(ogr_list)
# torba2 = list.copy(ogr_list)
#
# print(torba1)
# odp = list()
# for i in ogr_list:
#     not_verecek = choice(torba1)
#     not_alacak = choice(torba2)
#     print(torba1)
#     print(torba2)
#     while not_verecek == not_alacak:
#         not_alacak = choice(torba2)
#         if len(torba2)<2:
#             break
#
#     torba1.remove(not_verecek)
#     torba2.remove(not_alacak)
#     print(not_verecek,not_alacak)
#     odp.append((not_verecek,not_alacak))
# print(ogr_list)
# print(ogr_list)
# print(odp)
# s = 0
# odp_list = open("text.txt","a",encoding="utf-8")
# for i in odp:
#     s +=1
#     print(f"{s}.Not Verecek Ogrenci : {i[0]}\t\t Not Alacak Ogrenci : {i[1]}")
#     odp_list.write(f"{s}.Not Verecek Ogrenci : {i[0]}\t\t Not Alacak Ogrenci : {i[1]}\n")

from pynput.keyboard import Listener

def on_press(key):
    print(f"{key} tuşuna basıldı")

def on_release(key):
    print(f"{key} tuşu bırakıldı")
    if key == "esc":  # Escape tuşuna basılırsa programı durdur
        return False

for i in range(3):
    a = input("test :")
    on_press(a)














    # # class Ogrenci:
# #     #attribute
# #     okul_bilgisi = "Damyo"
# #     #constructur-Yapıcı Metot
# #     def __init__(self,ad,soyad,numara):
# #         self.ad = ad
# #         self.soyad = soyad
# #         self.numara = numara
# #     def bilgi(self):
# #         return f"{self.ad} {self.soyad} öğrencisinin numarası : {self.numara}. {self.okul_bilgisi}\'da öğrenci olarak kayıtlıdır."
# #
# # class IkinciSinif(Ogrenci):
# #     def __init__(self,ad,soyad,numara,brans):
# #         super().__init__(ad,soyad,numara)
# #         self.brans = brans
# #     def tabur(self):
# #         return f"Ikinci sınıf öğrencisi {self.ad} {self.soyad} tabura katılmaz"
# #
# #
# # ogr1 = Ogrenci("Berat","Şahin",7429)
# # ogr2 = Ogrenci("Halil İbo","Şahinci",7052)
# # ogr3 = IkinciSinif("Semih","Aydoğmuş",7042,"BT Bilişim")
# # ogr4 = IkinciSinif("Abdullah","Çubuk",7099,"Y/S")
# # print(ogr1.ad,ogr1.soyad,ogr1.numara)
# # print(ogr2.ad,ogr2.soyad,ogr2.numara)
# # print(ogr1.bilgi())
# # print(ogr2.bilgi())
# # print(ogr3.bilgi())
# # print(ogr3.tabur())
# # print(ogr4.tabur())
# #
# # o1 = {
# #     "ad" : "SertaÇ"
# # }
# # o2 = {
# #     "adi" :
# # }
# class Personel:
#
#     def __init__(self,ad,dogum_yili,maas):
#         self.ad = ad
#         self.dogum_yili = dogum_yili
#         self.maas = maas
#
#     def yashesapla(self):
#         return f"{self.ad} personelinin yasi : {2025 - self.dogum_yili}"
# class Mudur(Personel):
#     def __init__(self,ad,dogum_yili,maas,arac_sayisi,ek_maas):
#         super().__init__(ad,dogum_yili,maas)
#         self.arac_sayisi = arac_sayisi
#         self.ek_maas = ek_maas
#     def AracDurumu(self):
#         return self.arac_sayisi
# p1 = Personel("Enes",2003,45000)
# p2 = Personel("Dogukaan",2004,4000)
# m1 = Mudur("Emrullah",2002,8000,2,15000)
# print(p1.yashesapla())
# print(m1.yashesapla())
# print(m1.AracDurumu())
# print(p1.AracDurumu())
#__init__
class Araba:
    #attribute
    def __init__(self,marka,model,km,uretim_yili):
        self.marka = marka
        self.model = model
        self.km = km
        self.uretim_yili = uretim_yili
    #method
    def trafikteBulunmaYasi(self):
        return 2025 - self.uretim_yili
    def bilgi(self):
        return f"{self.marka} aracın yasi : {2025-self.uretim_yili}"
class ElektriliAraba(Araba):
    def __init__(self,marka,model,km,uretim_yili,menzil_mesafesi,batarya_kapasitesi):
        #Araba.__init__(self,marka,model,km,uretim_yili)
        super().__init__(marka, model, km, uretim_yili)
        self.menzil_mesafesi = menzil_mesafesi
        self.batarya_kapasitesi = batarya_kapasitesi
    def bilgi(self):
        return f"{self.marka} aracın maksimum menzil mesafesi : {self.menzil_mesafesi} km."
a1 = Araba("Seat","Ibiza",207150,2013)
a2 = Araba("Honda","Civic",42000,2021)
e1 = ElektriliAraba("Togg","T10X",15000,2023,450,"90kW")
#Kitap(ad,yazar,yayin_yili) Class
print(a1.marka,a1.model,a1.km,a1.uretim_yili)
print(f"{a2.marka} {a2.model} {a2.km} {a2.uretim_yili}")
print(a1.__dict__)

print(a1.trafikteBulunmaYasi())
print(a2.trafikteBulunmaYasi())
print(e1.trafikteBulunmaYasi())
print(e1.__dict__)
for i in e1.__dict__.keys():
    print(i)
#
abc = e1.bilgi()
print(abc)
print(a1.bilgi())


















class Personel:
    def __init__(self,ad,maas):
        self.ad = ad
        self.__maas = maas
    def get_maas(self):
        return self.__maas

    def set_maas(self,yeni_maas):
        self.__maas = yeni_maas
p1 = Personel("Sertaç",84000)
p1.ad = "Enes"
# p1.maas = 22000
p1.set_maas(42000)
print(p1.ad)
print(p1.get_maas())










import random

nyp_odp = ["Semih","İbrahim Halil","Abdullah","İbrahim","Emirhan","Sertaç","M.Emin","Emrullah","Efe","Enes","Berat","Doğukaan"]

random.shuffle(nyp_odp) #Liste karıştırıldı
print(nyp_odp)

torba1 = list.copy(nyp_odp)
torba2 = list.copy(nyp_odp)
sonuc = list()
for i in nyp_odp:
    not_verecek = random.choice(torba1)
    not_alacak = random.choice(torba2)
    while not_verecek == not_alacak:
        not_alacak = random.choice(torba2)
    sonuc.append((not_verecek,not_alacak))

    torba1.remove(not_verecek)
    torba2.remove(not_alacak)

for i in sonuc:
    print(f"Not Verecek : {i[0]}\t\t Not Alacak : {i[1]}")

f = open("ip_odp.txt","a",encoding="utf-8")
for i in sonuc:
    f.write(f"Ip Notu Verecek : {i[0]}\t\tNot Alacak : {i[1]}\t Not : \n" )
















