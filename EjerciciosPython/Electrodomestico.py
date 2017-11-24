class Electrodomestico:

    def __init__(self, precioBase, color, consumoEnergetico, peso):
        self.precioBase=precioBase
        self.color=color
        self.consumoEnergetico=consumoEnergetico
        self.peso=peso
        self.comprobarConsumoEnergetico(self.consumoEnergetico.upper())
        self.comprobarColor(self.color.lower())

    def getPrecioBase(self):
        return self.precioBase

    def getColor(self):
        return self.color

    def getConsumoEnergetico(self):
        return self.consumoEnergetico

    def getPeso(self, peso):
        self.peso=peso

    def setPrecioBase(self, precioBase):
        self.precioBase=precioBase

    def setColor(self, color):
        self.color=color

    def setConsumoEnergetico(self, consumoEnergetico):
        self.consumoEnergetico=consumoEnergetico

    def setPeso(self, peso):
        self.peso=peso

    def comprobarConsumoEnergetico(self, a):
        if a == 'A':
            self.consumoEnergetico='A'
            return 100
        elif a == 'B':
            self.consumoEnergetico = 'B'
            return 80
        elif a == 'C':
            self.consumoEnergetico = 'C'
            return 60
        elif a == 'D':
            self.consumoEnergetico = 'D'
            return 50
        elif a == 'E':
            self.consumoEnergetico = 'E'
            return 30
        elif a == 'F':
            self.consumoEnergetico = 'F'
            return 10
        else:
            self.consumoEnergetico = 'F'

    def comprobarColor(self, color):
        if color == "blanco":
            self.color="blanco"
        elif color == "negro":
            self.color = "negro"
        elif color == "rojo":
            self.color = "rojo"
        elif color == "azul":
            self.color = "azul"
        elif color == "gris":
            self.color = "gris"
        else:
            self.color = "blanco"

    def comprobarTamanio(self, tamanio):
        if tamanio <= 19:
            return 10
        elif tamanio >19 and tamanio <=49:
            return 50
        elif tamanio >49 and tamanio <=79:
            return 80
        elif tamanio >79:
            return 100

    def precioFinal(self):
        precioFinal = (self.precioBase) + self.comprobarConsumoEnergetico(self.getConsumoEnergetico()) + self.comprobarTamanio(self.peso)
        return precioFinal

class Lavadora(Electrodomestico):

    def __init__(self, carga, precioBase, color, consumoEnergetico, peso):
        self.carga=carga
        self.precioBase=precioBase
        self.color=color
        self.consumoEnergetico=consumoEnergetico
        self.peso=peso
        self.comprobarConsumoEnergetico(self.consumoEnergetico.upper())
        self.comprobarColor(self.color.lower())

    def getCarga(self):
        return self.carga

    def setCarga(self, carga):
        self.carga=carga

    def precioFinal(self):
        if self.carga>30:
            return super(Lavadora, self).precioFinal()+50
        else:
            return super(Lavadora, self).precioFinal()

class Television(Electrodomestico):

    def __init__(self, resolucion, fourK, precioBase, color, consumoEnergetico, peso):
        self.resolucion=resolucion
        self.fourK=fourK
        self.precioBase=precioBase
        self.color=color
        self.consumoEnergetico=consumoEnergetico
        self.peso=peso
        self.comprobarConsumoEnergetico(self.consumoEnergetico.upper())
        self.comprobarColor(self.color.lower())

    def getResolucion(self):
        return self.resolucion

    def getFourK(self):
        return self.fourK

    def setResolucion(self, resolucion):
        self.resolucion=resolucion

    def setFourK(self, fourK):
        self.fourK=fourK

    def precioFinal(self):
        if self.resolucion>40 and self.fourK is True:
            return super(Television, self).precioFinal() + super(Television, self).precioFinal() * 0.3 + 50
        elif self.resolucion>40:
            return super(Television, self).precioFinal() + super(Television, self).precioFinal() * 0.3
        else:
            return super(Television, self).precioFinal()