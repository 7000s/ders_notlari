import random

nyp_odp = ["a","b","c","d","e","f","g","h","ı","i","k","l"]

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
