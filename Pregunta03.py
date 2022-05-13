#Diseñar un algoritmo que permita calcular una operación aritmética entre 2 valores introducidos y el signo correspondiente por teclado: si es el signo es + debe realizar una suma, si es el signo – debe realizar la resta, si es el signo / debe realizar la división, si es el signo * debe realizar la multiplicación, si es el signo ^ debe calcular la potencia; por otro lado, si introduce R debe permitir calcular la raíz cuadrada de un número, si introduce % debe permitir calcular el módulo de 2.
import os, math
numero1 = int(input("ingrese primer número: "));
numero2 = int(input("ingrese segundo numero: "));
operacion = input("suma, resta, división, multiplicación, raiz_cuadrada, potencia: ");
 
if operacion == "+":
    print(numero1 + numero2)
elif operacion == "-":
    print(numero1 - numero2)
elif operacion == "/":
    print(numero1 / numero2)
elif operacion == "*":
    print(numero1 * numero2)
elif operacion == "R":
    print(math.sqrt(numero1))
    print(math.sqrt(numero2))
elif operacion == "^":
    print(numero1 ** (2))
    print(numero2 ** (2))