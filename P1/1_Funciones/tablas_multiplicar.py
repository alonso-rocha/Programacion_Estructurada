'''
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- Sin estructuras de control
2.- Sin funciones
'''



num=int(input("Ingrese el numero de la tabla de multiplicar "))
multi=num*1
print(f"{num} x 1 = {multi}")
multi=num*2
print(f"{num} x 2 = {multi}")
multi=num*3
print(f"{num} x 3 = {multi}")
multi=num*4
print(f"{num} x 4 = {multi}")
multi=num*5
print(f"{num} x 5 = {multi}")
multi=num*6
print(f"{num} x 6 = {multi}")
multi=num*7
print(f"{num} x 7 = {multi}")
multi=num*8
print(f"{num} x 8 = {multi}")
multi=num*9
print(f"{num} x 9 = {multi}")
multi=num*10
print(f"{num} x 10 = {multi}")







#version 2
'''
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- con estructuras de control
2.- Sin funciones
'''

i=1
num=int(input("Ingrese el numero de la tabla de multiplicar "))
for i in range(1,11):
    multi=num*i
    print(f"{num} x {i} = {multi}")
    







#version 3
'''
Crear un programa que calcule e imprima la tabla de multiplicar del 2

Restricciones:
1.- con estructuras de control
2.- con funciones

'''

i=1
num=int(input("Ingrese el numero de la tabla de multiplicar "))
def multi (num,i):
    return (num*i) 

for i in range(1,11):
    multipli= multi(num,i)
    print(f"{num} x {i} = {multipli}")

while i<11:
    multipli= multi(num,i)
    print(f"{num} x {i} = {multipli}")

    

####

def tabla(numero):
    num=numero
    respuesta=""
    for i in range(1,11):
        multi=num*i
        respuesta += f"\t{num} x {i} = {multi}\n"
    return respuesta

num=int(input("Ingrese el numero de la tabla de multiplicar: "))

resultado = tabla(num)
print (f"{resultado}")
  