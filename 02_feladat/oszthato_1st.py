ezekaszamok = []

def oszthato():
    
    for szam in range(100, 1000):
        if szam % 7 == 0 and szam % 3 != 0:
            ezekaszamok.append(szam)

oszthato()


def atlag(szamok):
    osszeg = 0
    osszeg = sum(szamok)

    mennyiazannyi = len(szamok)
    print(osszeg / mennyiazannyi)



atlag(ezekaszamok)+


