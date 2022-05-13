#Tiendas Plaza Norte desea un programa que permita calcular el IVG de la venta de sus artefactos además desea hacer un descuento de 10% cuando el monto base de venta supera los 2000 soles, mientras que si el monto supera los 1000 desea hacer un descuento del 5% Y si supera los 500 soles realiza un descuento del 2%, El algoritmo debe permitir calcular el IGV, el descuento y el monto total a pagar
import os

precio = float (input ("Ingresa el valor de precio: "))
descuento=0
if precio>2000:
    descuento=precio*0.10
if precio>1000 and precio<=2000:
    descuento=precio*0.5
if precio>500 and precio<=1000:
    descuento=precio*0.2
costo=precio-descuento
IGV=costo*0.18
print ("IGV: "+ repr (IGV))
print ("Valor de costo: " + repr (costo))
print ("Valor de descuento: " + repr (descuento))
print ()