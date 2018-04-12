# -*- coding: cp1254 -*-

#main 12 04 2018
import modul
print(modul.ad)

# from modul import ad  sadece ad yükler
# from modul import ad as adı

sayi = input("sayi gir:")
sonuc = modul.karekokAl(sayi)
print(sayi," karekoku= ",sonuc)

print(dir(modul)) #mdoul ici kullanılacaklar
