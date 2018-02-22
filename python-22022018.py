def main():
    state = input("ciro için 1 katma değer için 2 yaz : ")
    state = int(state)
    if(state == 1):
        ciro()
    elif(state ==2):
        KatmaDegerciro()
        
def turnint(liste):
    global createdDict
    createdDict={}
    for key, value in liste.items():
        createdDict[key] = int(value)
        
def ciro():
    miktar =input("Satış Miktarı Giriniz : ")
    miktar = int(miktar)
    birimfiyat  = input("Birim satış fiyatı giriniz : ")
    birimfiyat = int(birimfiyat)
    
    result = miktar*birimfiyat
    print("Cironuz :",result)

def KatmaDegerciro():
    miktar =input("Satış Miktarı Giriniz : ")
    
    hmm =input("ham madde maliyeti Giriniz : ")

    bog =input("Bakım Onarım Gideri Giriniz : ")

    sg  =input("Sevkiyat gideri Giriniz : ")

    sevg =input("Satın alınan hizmet giderleri Giriniz : ")

    liste={'miktar':miktar,'hmm':hmm,'bog':bog,'sg':sg,'sevg':sevg}
    turnint(liste)
    
    result = createdDict["miktar"]-( createdDict["hmm"]+createdDict["bog"]+createdDict["sg"]+createdDict["sevg"] )
    print("Katma değerli Cironuz :",result)
    
while (True):
    try:
        print("Ciro hesaplama programı")
        main()
    except KeyboardInterrupt: 
         interruptState = input("Çıkmak için e tuşla devam etmek için c : ")
         if(interruptState == "e"):
             exit()
         elif (interruptState == "c" ):
             pass
