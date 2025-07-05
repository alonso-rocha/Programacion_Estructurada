'''
List (Array)
son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder
a los valores de hace con un indice numerico.

Nota : sus valores si son modificables

La lista es una colección ordenada y modificable. Permite miembros duplicados.
'''

import os
os.system("cls")

#Funciones más comunes en las listas

paises = ["Mexico","Brasil", "España", "Canada"]
numeros = [23,45,8,24, 23, 56]
varios = ["hola", 2.1416, 33, True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)


#Recorrer una lista e imprimir el contenido
#1er forma
for i in paises:
    print(i)

lista="["
for i in paises:
    lista+=f"{i},"
print(lista+"]")

#2da forma
for i in range(0,len(paises)):
    print(paises[i])

lista="["
for i in range(0,len(paises)):
    lista+=f"{paises[i]},"
print(lista+"]")

#Ordenar los elementos de las listas   
os.system("cls")
print(paises)
print(numeros)
print(varios)

paises.sort()
print(paises)
numeros.sort()
print(numeros)

#dar la vuelta a las listas
varios.reverse()
print(varios)
paises.reverse()
print(paises)
numeros.reverse()
print(numeros)

#Buscar un elemento dentro de una lista
print("España" in paises)

#Incertar, anadir, agregar un elemento a una lista
os.system("cls")
print(paises)

#1er forma (se agrega al final)
paises.append("México")
print(paises)

#2da forma (elijes el lugar donde agregar)
paises.insert(1, "México")
print(paises)

#Borrar, eliminar, suprimir, quitar un elemento de la lista

os.system("cls")
print(paises)

#1er forma (elimina el elemento de la posicion seleccionada, si no encuentra nada en esa pocicion da error)
paises.pop(0)
print(paises)

#2da forma (el dato busca el primer dato identico y lo elimina, si no encuentra nada da error)
paises.remove("México")
print(paises)

paises.sort()

#Obtener el indice o la posición en la cual se encuentra un elemento
os.system("cls")
print(paises)

posicion=paises.index("Canada")
print(posicion)
paises.pop(posicion)
print(paises)

#Contar el numero de veces que un elemento aparece en una lista
os.system("cls")
print(numeros)

cuantas=numeros.count(45)
print(cuantas)

cuantas=numeros.count(23)
print(cuantas)

cuantas=numeros.count(233)
print(cuantas)

#Unir el contenido de una lista en otra

os.system("cls")
print(numeros)

numeros2=[100,200]
print(numeros2)

#Crear un programa que una las listas numericas 1 y 2 e imprima el contenido de lista resultante en forma decendente
os.system("cls")
numeros.extend(numeros2)
print(numeros)

numeros.sort()
numeros.reverse()
print(numeros)

