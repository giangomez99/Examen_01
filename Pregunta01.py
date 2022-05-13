#Diseñe un algoritmo que permita determinar el nivel del perfil de ingreso de un postulante con la  que obtiene una vacante a la carrera de ingeniería de Sistemas; considerando que, si su nota es mayor  o igual a 17 su nivel es 4, si la nota es menor de 17 y mayor o igual a 14 su nivel es 3, si su nota es  menor a 14 y mayor o igual a 11 su nivel es 2; mientras que si su nota es menor de 11 ya no puede  obtener la vacante y por ende también está en el nivel 1.
import os

nota = float (input ("Ingresa el valor de la nota: "))
if nota>=17:
  print("Nivel 4")
if nota>=14 and nota<17:
  print("Nivel 3")
if nota>=11 and nota<14:
  print("Nivel 2")
if nota<11:
  print("Nivel 1")