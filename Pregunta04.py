#Secretaría de salud requiere un algoritmo que permita determinar qué tipo de vacuna (A, B o C)  aplicar a una persona, considerando que, si es mayor de 70, sin importar el sexo, se le aplica el tipo C;  si tiene entre 16 y 69 años, y es mujer se le aplica el tipo B, y si es hombre, la A; sí es menor de 16 años, se aplica el tipo A sin importar el sexo.
import os, sys

edad = int (input ("Ingresa el valor de edad: "))
print ("Selecciona el valor de sexo:")
print ("\t1.- mujer")
print ("\t2.- hombre")
sys.stdout.write ("\t")
sexo = 0
while sexo<1 or sexo>2:
    sexo = int (input (': '))
    if sexo<1 or sexo>2:
        sys.stdout.write ("Valor incorrecto. Ingresalo nuevamente.")
if (sexo==2 and edad>=16 and edad<70) or edad<16:
    print ("A")
if sexo==1 and edad>=16 and edad<70:
    print ("B")
if edad>70:
    print ("C")