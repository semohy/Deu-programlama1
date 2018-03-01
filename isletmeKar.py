def main():
    ABC()



def ABC():
    #adam basi ciro hesabı
    totalCiro = int(input("Toplam Cironuz :"))
    toplamCalisan = int(input("Çalışan Sayısı"))

    abc = totalCiro / toplamCalisan

    if(abc >= 100):
        print("Başarılı")
    elif(50 < abc < 100 ):
        print("Normal")
    else:
        print("Başarısız")


while True:
    try:
        main()
    except KeyboardInterrupt:
        interruptState = input("Çıkmak için e tuşla devam etmek için c : ")
        if(interruptState == "e"):
             exit()
        elif (interruptState == "c" ):
             pass

