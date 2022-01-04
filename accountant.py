dozwolone_operacje = ("saldo", "zakup", "sprzedaz", "konto", "magazyn", "przegląd", "stop")
operacje=[]
towary=dict()
wartosc_saldo = 0
while True:
    argument = str(input())
    if argument not in dozwolone_operacje:
       print("błąd")
       break
    if argument == "saldo":
        operacje.append(argument)
        if wartosc_saldo:
            wartosc_saldo += int(input())
        else:
            wartosc_saldo = int(input())    
        operacje.append(wartosc_saldo)
        komentarz = str(input())
        operacje.append(komentarz)
    elif argument =="zakup":
        operacje.append(argument)
        identyfikator = str(input())
        operacje.append(identyfikator)
        cena = int(input())
        operacje.append(cena)
        liczba = int(input())
        towary[identyfikator] = liczba
        operacje.append(liczba)
        wartosc_saldo = wartosc_saldo - (cena*liczba)
        if wartosc_saldo < 0:
            print("\nbłąd - saldo ujemne\n")
            break
    elif argument =="sprzedaz":
        operacje.append(argument)
        identyfikator = str(input())
        operacje.append(identyfikator)
        cena = int(input())
        operacje.append(komentarz)
        liczba = int(input())
        operacje.append(liczba)
        towary[identyfikator] -= liczba
        if towary[identyfikator] <0:
            print(f"\nstan towaru {identyfikator} jest mniejszy od 0\n")
            break
        wartosc_saldo = wartosc_saldo + (cena*liczba)
    elif argument =="stop":
        operacje.append(argument)
        break        
for i in operacje:
    print (i)  
print (f"\nstan magazynu: \n {towary}")
print (f"\nwartość saldo:{wartosc_saldo}")
