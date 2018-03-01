def main():
    inpt = input("Sayı GirinTek mi Çift mi:\n")
    inptControl(inpt)
    inpt = int(inpt)
    kontrol(inpt)


def kontrol(inpt):
    kalan = inpt % 2
    if (kalan == 0):
        print ("Çift!!")
    else:
        print("Tekk!!")

def inptControl(inpt):
    number = ["0","1","2","3","4","5","6","7","8","9"]
    for x in inpt[:]:
        if x not in number:
            print("Sayı Gir SAYI \n")
            main()
while True:
    try:
        print("Uzun Eşşek oyunu ")
        main()
    except KeyboardInterrupt:
        interruptState = input("Çıkmak için e tuşla devam etmek için c : ")
        if(interruptState == "e"):
             exit()
        elif (interruptState == "c" ):
             pass
