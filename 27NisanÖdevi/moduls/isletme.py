#isletme modulu
class isletme:
    def karHesabi(text1,text2):
        gelir = int(input(text1))
        gider = int(input(text2))

        result = gelir-gider
        return result
    
    def abCiro(): #adam bası ciro
         tc = int(input("Toplam Ciro Giriniz :"))
         tcs = int(input("Toplam Çalışan Sayısı Giriniz :"))

         result = tc/tcs
         return result

class bilanco:
    def __init__(self,entity): # entity is a dictionary or json data
        
        self.common = {}

        active_total  = 0
        passive_total = 0

        for x in entity:
            for y in entity[x]:
                #1,2, gibi numaraları alır 3 ten küçükler aktiftir 3+ pasif
                if(y.find("1") or y.find("2") ): #aktif
                    for t in entity[x][y]:   
                        active_total +=  entity[x][y][t]
                elif(y.find("3") or y.find("4")or y.find("5")):#pasif
                    print(y.find("1"))
                    for t in entity[x][y]:
                        passive_total +=  entity[x][y][t]
                        print(entity[x][y][t])
                    #self.common["passive"] = passive_total
        self.common["active"] = active_total
        self.common["passive"] = active_total
        print(self.common)
        
