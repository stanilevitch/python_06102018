print(locals())
print(globals())
# ---------------------------------------------------------------------------------
return - kończy funkcje
www.packtpub.com / zcientific computing with python3
przeróbki zadna na funkcyjne - zp oprzeniego zjazdu;
print i return z funkcji by zrobić assertion - czuy wydrukowało sie to co trzeba

zad.5
dane = pobieranie_danych()
*dane (rozpakowanie tupli)
koszt = obliuczenie_kosztu(*dane)

zad.10 przeróbka
dane = podaj_liczby_i_operacje()
kalkulator(*dane)

# obsługa błędu
def prezentuj_wynik():
    danie = podaj_liczby_i_operacje()
    try:
        wynik = kalkulator(*dane)
    except ValueError:
        wynik = "Operacja niedozwolona"
    print(wynik)

zad.13 przeróbka
