'''f = open("./03_feladat/konyvek.txt", "r", encoding='utf-8')
print(f.read())
print(f.readline())

for sor in f:
    print(sor)

f.close()'''

konyvek = []
with open('./03_feladat/konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        nev = adatok[0]
        szul_ev = adatok[1]
        if adatok[2]:
            hal_ev = adatok[2]
        else:
            hal_ev == 2005
        nemzetiseg = adatok[3]
        cim = adatok[4]
        helyezes = adatok[5]
        # konyv = {'nev': adatok[0],
        #         'szulEv': adatok[1],
        #         'halEv': adatok[2],
        #         'Nemzetiseg': adatok[3],
        #         'cim': adatok[4],
        #         'helyezes': adatok[5]}
        konyvek.append([nev, szul_ev, hal_ev, nemzetiseg, cim, helyezes])
    
#print(f'{konyvek=}')
def konyvszam():
    print(f"3.2. feladat: Az állományban {len(konyvek)} db könyv adatai szerepelnek.")

def legjobbmagyar():
    legjobbhu = None
    for konyv in konyvek:
        if konyv[3] == 'magyar':
            if legjobbhu is None or konyv[5] < legjobbhu[5]:
                legjobbhu =  konyv

    print(f"3.3 feladat: A legjobb helyezést elért magyar könyv: {legjobbhu[0]}: {legjobbhu[4]}")

def nemetiro():
    nemetiro = False
    for konyv in konyvek:
        if konyv[3] == 'német':
            nemetiro = True
    
    if nemetiro == True:
        print("3.4 feladat: A listában szerepel német író könyve.")
    else:
        print("3.4 feladat: A listában NEM szerepel német író könyve.")

def oregek():
    old = []
    eletkor = int(konyv[1]) - int(konyv[2])
    for konyv in konyvek:  
        if eletkor > 90:
            old.append(konyv[0])
    print(f"Ők 90-nél öregebbek: {old}")


konyvszam()
legjobbmagyar()
nemetiro()
oregek()