print("""
**********************************
1-Para çekme
2-Para yatırma
3-Bakiye sorgulma
4-Programdan çıkma
""")
sys_şifre="1238"
Bakiye=1000
while True:
    şifre=input("Şifrenizi giriniz:")
    if(şifre!=sys_şifre):
        print("şifreniz yanlış tekrar deneyiniz")
    elif(şifre==sys_şifre):
        print("şifreniz doğru yapmak istediğiniz işlemi seçiniz..")
        while True:
            işlem = int(input("İşleminizi seçiniz..."))
            if (işlem == 1):

                para_çekme = int(input("Çekmek istediğiniz miktari giriniz : "))
                if(Bakiye-para_çekme<0):
                    print("Yeterli bakiyeniz yok")
                    continue
                Bakiye-=para_çekme
                print("Yeni bakiyeniz",Bakiye)
            elif(işlem==2):
                para_yatırma=int(input("Yatıracağınız miktarı yazınız : "))
                Bakiye+=para_yatırma
                print("Yeni bakiyeniz",Bakiye)
            elif(işlem==3):
                print("Bakiyeniz:",Bakiye)

            elif(işlem==4):
                print("Hoşçakalın.. :)")
                break
            else:
                print("Geçersiz işlem Tekrardan deneyiniz")
