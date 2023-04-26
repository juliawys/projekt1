def funkcja(x):
    if x == 1:
        return 1
    else:
        return x + funkcja(x-1)
    
wynik1 = funkcja(5)
print(wynik1)
wynik2 = funkcja(10)
print(wynik2)
wynik3 = funkcja(1)
print(wynik3)
wynik4 = funkcja(23)
print(wynik4)

def potega(liczba= 2, wykladnik=3):
    if wykladnik == 0:
        return 1
    else:
        return liczba * potega(liczba, wykladnik -1)

wynik = potega()
print(wynik)
