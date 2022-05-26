
sys_password = "1234"
balance = 1000
money_withdrawal_operation_id = 10
money_deposit_operation_id = 2
balance_check_operation_id = 3
exit_program_operation_id = 4

print("""
**********************************
1-Para çekme
2-Para yatırma
3-balance sorgulma
4-Programdan çıkma
""")
while True:
    password = input("passwordnizi giriniz:")
    if(password != sys_password):
        print("passwordniz yanlış tekrar deneyiniz")
    elif(password == sys_password):
        print("passwordniz doğru yapmak istediğiniz operationi seçiniz..")
        while True:
            operation = int(input("operationinizi seçiniz..."))
            if (operation == money_withdrawal_operation_id):

                money_withdrawal = int(input("Çekmek istediğiniz miktari giriniz : "))
                # noinspection PyRedundantParentheses
                if(balance - money_withdrawal < 0):
                    print("Yeterli balanceniz yok")
                    continue
                balance -= money_withdrawal
                print("Yeni balanceniz", balance)
            elif(operation == money_deposit_operation_id):
                deposit_money = int(input("Yatıracağınız miktarı yazınız : "))
                balance += deposit_money
                print("Hesabınıza şu miktarda para yatırılmıştır : ", deposit_money)
                print("Yeni balanceniz", balance)
            elif(operation == balance_check_operation_id):
                print("balanceniz:", balance)

            elif(operation == exit_program_operation_id):
                print("Hoşçakalın.. :)")
                break
            else:
                print("Geçersiz operation Tekrardan deneyiniz")
