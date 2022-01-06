import sys
dozwolone_operacje = ("saldo", "zakup", "sprzedaz", "stop")
operacje=[]         #tu będe zbierał operacje do wydruku
towary=dict()       #do operacji "magazyn"
suma_saldo = 0   #do operacji "konto"
while True:
    argument = str(input())
    if argument not in dozwolone_operacje:
       print("błąd - niedozwlona akcja\nprogram zakończy działanie")
       break
    if argument == "saldo":                                       #funkcja saldo
        wartosc = int(input("wartość"))
        if suma_saldo:
            suma_saldo += wartosc
        else:
            suma_saldo = wartosc   
        komentarz = str(input("komentarz"))
        operacje.append([argument, wartosc, komentarz])
        #operacje.append(suma_saldo)
        #operacje.append(komentarz)
    elif argument =="zakup":                                     #funkcja zakup
        identyfikator = str(input("id"))
        cena = int(input("cena"))
        liczba = int(input("ilosc"))
        if suma_saldo - cena * liczba <0:
            print("\nbłąd - saldo nie może być ujemne\n")
            continue
        else:
            suma_saldo -= cena * liczba 
            if towary[identyfikator]:
                towary[identyfikator] += liczba
            else:
                towary[identyfikator] = liczba      
            operacje.append(argument)
            operacje.append(identyfikator)
            operacje.append(cena)
            operacje.append(liczba)
    elif argument =="sprzedaz":                                 #funkcja sprzedaż
        identyfikator = str(input("id"))
        if identyfikator not in towary:
            print (f"\nnie mamy na stanie {identyfikator}\n") 
            continue   
        else:
            cena = int(input("cena"))
            liczba = int(input("ilosc"))
            if towary[identyfikator] - liczba < 0:
                print (f"nie wystarczająca ilość {identyfikator} na stanie")
                continue
            else:        
                towary[identyfikator] -= liczba
                suma_saldo += cena * liczba
                operacje.append(liczba)
                operacje.append(argument)
                operacje.append(identyfikator)
                operacje.append(komentarz)
    elif argument =="stop":
        operacje.append(argument)
        break   
    
if sys.argv[1] =="konto":                                       #funkcja konto
    print (f"\nwartość saldo:{suma_saldo}") 
elif sys.argv[1] =="magazyn":
    print (f"\nstan magazynu: \n {towary}")                     #funkcja magazyn    
elif sys.argv[1] =="przeglad":                                  #funkcja przeglad
    for i in range (int(sys.argv[2]),int(sys.argv[3])+1):
        print(*operacje[i], sep = "\n")




