#1. feladat
fogyasztas = int(input("Az autó fogyasztása [l/100 km]: "))
urtartalom = int(input("A benzintank űrtartalma [l]: "))
tavolsag = int(input("A megtenni kívánt távolság [km]: "))
megtett = urtartalom / fogyasztas * 100 

print(f"Az autó {megtett} km-t tud megtenni, ha tele tankkal indul.")

if megtett < tavolsag:
    print("Az út során kell tankolnunk.")
else:
    print("Az út során nem kell tankolnunk.")        