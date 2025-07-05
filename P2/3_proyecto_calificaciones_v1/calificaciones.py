
# lista=[
#
#
# 
#           ]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprima cualquier tecla para continuar")

def menu_principal():
    print("...::: Sistema de Gestión de Calificaciones :::...\n1.- Agregar \n2.- Mostrar \n3.- Calcular promedios \n4.- SALIR ")
    opcion=input("\t Elige una opción (1-4):  ").upper()
    return opcion

def agregar_calificaciones(lista):
    borrarPantalla()
    print("..:::Agregar Calificaciones :::..")
    nombre=input("Nombre del alumno : ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        bandera=True
        while bandera:
            try:
                cal=float(input(f"Calificación {i} : "))
                if cal >= 0 and cal <= 10:
                    calificaciones.append(cal)
                    bandera=False
                else:
                    print("Ingrese un valor comprendido entre el 0 y 10")
            except ValueError:
                print("Ingrese un valor númerico")
    lista.append([nombre] + calificaciones)
    print("Acción realizada con éxito")

def mostrar_calificaciones(lista):
    borrarPantalla()
    print("Mostrar Calificaciones")
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Calif.1":<10}{"Calif.2":<10}{"calif.3":<10}")
        print("-"*50)
        for fila in lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
        print("-"*50)
        print(f"Son {len(lista)} alumnos")
    else:
        print("No hay calificaiones en el sistema")

def calcular_calificaciones(lista):
    borrarPantalla()
    print("Promedios de Alumnos")
    promedio_clase=0
    if len(lista)>0:
        print(f"{"Nombre" :<15}{"Promedio":<10}")
        print("-"*30)
        for fila in lista:
            promedio=((fila[1])+(fila[2])+(fila[3]))/3
            print(f"{fila[0]:<15}{promedio:.2f}")
            promedio_clase+=promedio
        print("-"*30)
        print(f"El promedio del grupo es : {(promedio_clase/len(lista)):.2f}")
    else:
        print("No hay calificaiones en el sistema")


