import sys
dozwolone_operacje = ("saldo", "zakup", "sprzedaz", "stop")
operacje=[]         #tu będe zbierał operacje do wydruku
towary=dict()       #do operacji "magazyn"
suma_saldo = 0   #do operacji "konto"
while True:
    argument = str(input())
    if argument not in dozwolone_operacje:
       print("błąd - niedozwolona akcja\nprogram zakończy działanie")
       break
    if argument == "saldo":                                       #funkcja saldo
        wartosc = int(input())
        if suma_saldo:
            suma_saldo += wartosc
        else:
            suma_saldo = wartosc   
        komentarz = str(input())
        operacje.append([argument, wartosc, komentarz])
    elif argument =="zakup":                                     #funkcja zakup
        identyfikator = str(input())
        cena = int(input())
        liczba = int(input())
        if suma_saldo - cena * liczba <0:
            print("\nbłąd - saldo nie może być ujemne\n")
            continue
        else:
            suma_saldo -= cena * liczba 
            if identyfikator in towary:
                towary[identyfikator] += liczba
            else:
                towary[identyfikator] = liczba     
            operacje.append([argument, identyfikator, cena, liczba])
    elif argument =="sprzedaz":                                 #funkcja sprzedaż
        identyfikator = str(input())
        if identyfikator not in towary:
            print (f"\nnie mamy na stanie {identyfikator}\n") 
            continue   
        else:
            cena = int(input())
            liczba = int(input())
            if towary[identyfikator] - liczba < 0:
                print (f"nie wystarczająca ilość {identyfikator} na stanie")
                continue
            else:        
                towary[identyfikator] -= liczba
                suma_saldo += cena * liczba
                operacje.append([argument, identyfikator, cena, liczba])
    elif argument =="stop":
        operacje.append(argument)
        break   

if sys.argv[1] =="saldo":  
    print (suma_saldo*2)
elif sys.argv[1] =="sprzedaz":   
    print (suma_saldo*3)  
elif sys.argv[1] =="zakup": 
    print (suma_saldo)
elif sys.argv[1] =="konto":                 #działa
    print (f"\nwartość saldo:{suma_saldo}") 
elif sys.argv[1] =="magazyn":       
    print (f"\nstan magazynu: \n {towary}")   
elif sys.argv[1] =="przeglad":              #działa
    for i in range (int(sys.argv[2]),int(sys.argv[3])+1):
        print(*operacje[i], sep = "\n")
#print (operacje[-1])

        




