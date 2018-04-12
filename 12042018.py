# Arrayler 12.04.2018
cars = ['volvo','bmw','mercedes']
for i in cars:
    print(i)

for i in range(2,5):
    print(i)

for u in range(2,len(cars)):
    print(cars[u])
cars.remove("mercedes")
print(cars)
x = cars.pop(0)
print("Silinen",x," Yeni liste:",cars)

cars = ['volvo','bmw','mercedes']

x = cars.pop()
print("Silinen",x," Yeni liste:",cars) #sondakini siler değer döndürür

print("Bmw sayısı:",cars.count("bmw"))

cars.insert(1,"fiat")
print("fiat eklendi (1.index): ",cars)

cars.append("volkswagen")
print("volkswagen eklendi (son index): ",cars)

print("Tümü: ",cars[:])

print("Tümü 2 eleman dan sonrası: ",cars[2:])

print("Tümü 2,3,4 (4 dahil 1 hariç) ",cars[1:4])

dersler = [["ybs2008","veritabanı"],["ybs2006","programlama"]]
print(dersler)

print("programlama ders kodu: ",dersler[1][0])
print("programlama ders kodu 2.harf: ",dersler[1][0][1])

for ders in dersler:
    for i in range(len(ders)):
        print("ders kodu:",i)
