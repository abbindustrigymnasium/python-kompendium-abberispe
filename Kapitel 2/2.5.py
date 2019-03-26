korv = input("korv?")
vegan = input("vegansk?")
dryck = input("dryck?")
#hämtar värden

korvpris = (int(korv) / 8) * 20.95
veganpris = (int(vegan) / 4) * 34.95
dryckpris = int(dryck) * 13.95
#konverterar till pris

print("korv: " + str(korvpris) + ", vegan: " + str(veganpris) + ", dryck: " + str(dryckpris))
#printar ut