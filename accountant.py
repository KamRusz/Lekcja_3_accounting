dozwolone_operacje = ("saldo", "zakup", "sprzedaz", "konto", "magazyn", "przegląd", "stop")
operacje=[]
while True:
    argument = str(input())
    if argument not in dozwolone_operacje:
       print("błąd")
       break
    if argument == "saldo":
        operacje.append(argument)
        wartosc_saldo = int(input())
        operacje.append(wartosc_saldo)
        komentarz = str(input())
        operacje.append(komentarz)
    elif argument =="zakup":
        operacje.append(argument)
        identyfikator = str(input())
        operacje.append(identyfikator)
        komentarz = str(input())
        operacje.append(komentarz)
        liczba = int(input())
        operacje.append(liczba)
    elif argument =="sprzedaz":
        operacje.append(argument)
        identyfikator = str(input())
        operacje.append(identyfikator)
        komentarz = str(input())
        operacje.append(komentarz)
        liczba = int(input())
        operacje.append(liczba)
    elif argument =="stop":
        operacje.append(argument)
        break        
for i in operacje:
    print (i)        




