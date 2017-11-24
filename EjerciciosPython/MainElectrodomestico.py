import Electrodomestico

ob1 = Electrodomestico.Electrodomestico(100, "blanco", 'f', 10)
ob2 = Electrodomestico.Lavadora(10, 200, "gris", 'a', 20)
ob3 = Electrodomestico.Electrodomestico(300, "rojo", 'e', 30)
ob4 = Electrodomestico.Television(50, False,400, "azul", 'b', 40)
ob5 = Electrodomestico.Electrodomestico(500, "negro", 'd', 50)
ob6 = Electrodomestico.Lavadora(50, 600, "blanco", 'c', 60)
ob7 = Electrodomestico.Electrodomestico(700, "azul", 'f', 70)
ob8 = Electrodomestico.Television(39, True, 800, "gris", 'e', 80)
ob9 = Electrodomestico.Electrodomestico(900, "rojo", 'f', 90)
ob10 = Electrodomestico.Television(60, True, 1000, "negro", 'a', 100)

lista=[ob1, ob2, ob3, ob4, ob5, ob6, ob7, ob8, ob9, ob10]

totalElectrodomestico = 0
totalTv = 0
totalLavadora = 0
for e in lista:
    totalElectrodomestico = totalElectrodomestico + e.precioFinal()
    if type(e) is Electrodomestico.Lavadora:
        totalLavadora = totalLavadora + e.precioFinal()
    elif type(e) is Electrodomestico.Television:
        totalTv = totalTv + e.precioFinal()

print ("Electrodomesticos: "+str(totalElectrodomestico))
print ("Lavadoras: "+str(totalLavadora))
print("Tv: "+str(totalTv))