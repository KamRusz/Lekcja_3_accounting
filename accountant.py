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
    if argument == "saldo":                                                     #funkcja saldo
        wartosc = int(input())
        if suma_saldo:
            suma_saldo += wartosc
        else:
            suma_saldo = wartosc   
        komentarz = str(input())
        operacje.append([argument, wartosc, komentarz])
    elif argument =="zakup":                                                    #funkcja zakup
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
    elif argument =="sprzedaz":                                                 #funkcja sprzedaż
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
        operacje.append([argument])
        break 
argument = (sys.argv[1]) 
if argument =="saldo":                                                          #działa
    wartosc = (sys.argv[2])
    komentarz = (sys.argv[3])                 
    operacje.insert(-1,[argument,wartosc,komentarz])
    for i in range(len(operacje)):
        print(*operacje[i], sep = "\n")
elif argument =="sprzedaz":                                                     #działa
    identyfikator = (sys.argv[2])
    cena = int(sys.argv[3])
    liczba = int(sys.argv[4])
    if identyfikator not in towary:
        print (f"\nnie mamy na stanie {identyfikator}\n") 
    else:
        if towary[identyfikator] - liczba < 0:
            print (f"nie wystarczająca ilość {identyfikator} na stanie")
        else:        
            towary[identyfikator] -= liczba
            suma_saldo += cena * liczba
            operacje.insert(-1,[argument, identyfikator, cena, liczba])
            for i in range(len(operacje)):
                print(*operacje[i], sep = "\n")  
elif argument =="zakup":                                                        #działa
    identyfikator = (sys.argv[2])
    cena = int(sys.argv[3])
    liczba = int(sys.argv[4])
    if suma_saldo - cena * liczba <0:
        print("\nbłąd - saldo nie może być ujemne\n")
    else:
        suma_saldo -= cena * liczba 
        if identyfikator in towary:
            towary[identyfikator] += liczba
        else:
            towary[identyfikator] = liczba  
        operacje.insert(-1,[argument, identyfikator, cena, liczba])
        for i in range(len(operacje)):
            print(*operacje[i], sep = "\n")
elif argument =="konto":                                                        #działa
    print (f"\nwartość saldo:{suma_saldo}") 
elif argument =="magazyn":                                                      #kiełbasi się
    for i in range(2,len(sys.argv)):
    #for i in range(1):
        print(towary.get("rapsberry"))
        print(towary)

        
elif argument =="przeglad":                                                     #działa
    par2 = (sys.argv[2])
    par3 = (sys.argv[3])
    for i in range (int(par2),int(par3)+1):
        print(*operacje[i], sep = "\n")