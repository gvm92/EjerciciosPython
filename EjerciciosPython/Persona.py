class Persona:

    def __init__(self, nombre, edad, DNI, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.DNI = DNI
        self.sexo = sexo
        self.peso = peso
        self.altura = altura

    def calcularIMC(self):
        imc = (self.peso / (self.altura/100 * self.altura/100))
        print(imc)
        if imc < 18.5:
            return -1
        elif (imc >= 18.5 and imc <= 24.99):
            return 0
        elif imc > 25:
            return 1

    def mayorDeEdad(self):
        if self.edad < 18:
            return False
        else:
            return True

    def introducirSexo(self):
        if (self.sexo != "M" or self.sexo != "H"):
            self.sexo=print("Error, Introduce(M o H)")
        print(self.sexo)
        return self.sexo

    def generarDNI(self):
        import random
        self.dni = print(random.randint(0, 9), 8)
        print(self.dni)
        return self.dni

    def toString(self):
        return self

