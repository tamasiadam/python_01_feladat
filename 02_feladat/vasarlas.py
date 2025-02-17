forint = float(input("Kérem a termék árát forintban: "))
euro = float(input("Kérem a euro árfolamát: "))
egyenleg = float(input("Mennyi euróval rendelkezel: "))

if euro * egyenleg >= forint:
    print("A terméket meg tudod vásárolni!")
else:
    print("Nincs elég euród a termék megvásárlására!")

