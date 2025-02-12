ezekaszamok = []

for szam in range(100, 1000):
    if szam % 7 == 0 and szam % 3 != 0:
        ezekaszamok.append(szam)

def oszthato(szamok):
    osszeg = sum(szamok)
    darab = len(szamok)
    atlag = osszeg / darab
    return atlag

print(oszthato(ezekaszamok))

