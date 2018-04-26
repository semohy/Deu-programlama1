#main program

from moduls.isletme import *

def isletme_main():
    text1 = "Gelir Giriniz :"
    text2 = "Gider Giriniz :"
    result = isletme.karHesabi(text1,text2)

    if(result > 0):
        print(result," TL Kar")
    elif(result == 0):
        print(result," TL Başabaş")
    else:
        print(result," TL Zarar")

def bilanco_main():
    entity = {
        "aktif":{
            "1 donen varlıklar":{
                "100 Kasa" :20000,
                "101 alınan cek" :10000,
                "102 Bankalar" :5000,
                "121 alacak senet" :28000,
                "153 ticari mal" :65000
            },

            "2 duran varlıklar":{
                "252 Binalar" :150000,
                "254 Taşıtlar" :25000,
                "255 Demirbaşlar" :8000   
            }
        },

        "pasif":{
            "3 kvyk":{
                "300 Banka Kredileri": 42000,
                "320 Satıcılar": 60000
                },
            "4 uvyk":{
                "400 Banka Kredileri": 35000,
                "421 Borç Senetleri": 115000
                },
            "5 özkaynaklar":{
                "500 Sermaye Hesabı": 59000
                }
          }
        }

    bilanco(entity)
    
bilanco_main()

