"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")

paises=["Mexico","Brasil","España","Canada"]
print(paises)
print(paises[1])

paises={}
  










#ejemplo crear un programa que solicite los email de los alumnos de la utd almacenar en una lista y posteriormente mostrar en pantalla los email sin duplicados
emails=[]
resp="si"

while resp=="si":
    emails.append(input("Ingresa un email de la utd"))
    resp=input("deseas ingresa otro email").lower()


emails_set=set(emails)
emails=list(emails_set)
print(emails)    