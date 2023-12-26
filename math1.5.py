import time
import os
os.system("cls")
while True:
    os.system("cls")
    time.sleep(0.4)
    print("-------------")
    print("|CALCULADORA|")
    print("-------------")
    print("")
    print("|TABELA DE OPÇÕES|")
    print("")
    print("--------------------")
    print("| 1 - ADIÇÃO        |")
    time.sleep(0.3)
    print("| 2 - SUBTRAÇÃO     |")
    time.sleep(0.3)
    print("| 3 - MULTIPLICAÇÃO |")
    time.sleep(0.3)
    print("| 4 - DIVISÃO       |")
    print("--------------------")
    time.sleep(0.3)
    escolha2 = input("Escolha Uma Opção (1, 2, 3, 4): ")
    if escolha2 == "sair":
        os.system('exit')
    if escolha2 == "1":
        ad1 = int(input("primeiro numero: "))
        ad2 = int(input("segundo numero: "))
        res_ad = ad1 + ad2
        print(res_ad)
    if escolha2 == "2":
        sub1 = int(input("primeiro numero:"))
        sub2 = int(input("segundo numero:"))
        res_sub = sub1 - sub2
        print(res_sub)
    if escolha2 == "3":
        mult1 = int(input("primeiro numero:"))
        mult2 = int(input("segundo numero:"))
        res_mult = mult1 * mult2
        print(res_mult)
    if escolha2 == "4":
        div1 = int(input("primeiro numero:"))
        div2 = int(input("segundo numero:"))
        res_div = div1 / div2
        print(res_div)
    else:
        escolha1 = input("quer continuar?: ")
        escolha1_min = escolha1.lower()
    if escolha1_min == ("nao"):
        time.sleep(0.3)
        print("Até mais...")
        time.sleep(1)
        break
     