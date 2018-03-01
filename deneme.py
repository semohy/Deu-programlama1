def main():
    
    global ideal1
    global ideal2
    ideal1 = 23
    ideal2 = 25
    inpt = input("Değer Giriniz (derece) :\n")
    inpt = int(inpt)
    contHeat(inpt)
    print(ideal1.type())
def inptCont(inpt):
    pass
    
def contHeat(inpt):
    if (inpt in range(ideal1,ideal2+1) ):
        print("İdeal Sıcaklıkta \n")
    elif (inpt < ideal1):
        print (">>>>>>>>>Soğuk la bura <<<<<<<<<<\n")
    elif (inpt > ideal2):
        print(">>>>>>>>> Yanıyorsun Fuat abeyy <<<<<<<<<<<<<\n")

while True:
    try:
        print("Sıcaklık ölçücü Programı ")
        main()
    except KeyboardInterrupt:
        interruptState = input("Çıkmak için e tuşla devam etmek için c : ")
        if(interruptState == "e"):
             exit()
        elif (interruptState == "c" ):
             pass
    
    
