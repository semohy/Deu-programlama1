import time
import locale
import random

import os #dosya i�lemleri

time1 = time.ctime()
print(time1)

locale.setlocale(locale.LC_ALL,'Turkish_Turkey')
print(time.strftime("%a, %d %b %Y %H:%M:%S"))

sleeptime = 0
print(sleeptime," saniye sonra nick im yazacak")
time.sleep(sleeptime)
print("SEMOHY")

print(random.random())

print(random.randrange(0,100))

print(random.choice(['ali',"veli","zibidi"])) # liste elemanlarından rando döndürür




renk = '#'
while(len(renk) <= 6):
    x = random.choice('ABCDEF1234567890')
    renk += x

print(renk)

#for ile

renk = '#'
for i in range(6):
    x = random.choice('ABCDEF1234567890')
    renk += x

print(renk)

def zarAtar():
    x1 = random.randrange(1,7) # 1 -> min dahil 2-> max hari�
    x2 = random.randrange(1,7)
    
    return x1,x2

print(zarAtar())

dosyaAdi = input("dosya ad� giriniz")

if not dosyaAdi:
    print("dosya d� giriniz")
elif(os.path.exists(dosyaAdi) is True):
    print("Bu dosya var")
    print(open(dosyaAdi).read())
else:
    print("Dosya Yok!!!")
