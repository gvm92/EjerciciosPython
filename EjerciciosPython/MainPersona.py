import Persona

nombre=str(input("Introduce tu nombre: "))
edad=int(input("Introduce tu edad: "))
dni=str(input("Introduce tu DNI: "))
sexo=str(input("Introduce tu sexo (H/M): "))
peso=int(input("Introduce tu peso: "))
altura=float(input("Introduce tu altura en cm: "))
ob1 = Persona.Persona(nombre, edad, dni, sexo, peso, altura)
resImc=ob1.calcularIMC()
resEdad=ob1.mayorDeEdad();
if resImc==1:
    print("Gordooooooo")
elif resImc==0:
    print("Ta bien")
elif resImc==-1:
    print("Tienes que comer mas")
if resEdad==True:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
print("Nombre: "+str(ob1.nombre)+" Edad: "+str(ob1.edad)+" DNI: "+str(ob1.DNI)+" Sexo: "+str(ob1.sexo)+" Peso: "+str(ob1.peso)+" Altura: "+str(ob1.altura))
