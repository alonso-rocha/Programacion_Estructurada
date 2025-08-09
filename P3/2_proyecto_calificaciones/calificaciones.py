#lista = [
#        ["Ruben",10.0,8.9,9.1],
#        ["Andres",10.0,10.0,10.0],
#        ["Maria",10.0,10.0,10.0]        
#        ]


lista = []

import mysql.connector
from mysql.connector import Error 

lista = []

def conectar():
    try:
        conexion = mysql.connector.connect(
            host = "127.0.0.1",
            user = "root",
            password = "",
            database = "bd_calificaciones")
        return conexion
    except Error as e:
        print(f"El error que se presento es {e}")
        return None
          

def borrarPantalla():
       import os 
       os.system("cls")

def esperarTecla():
        input("Oprima cualquier telca para continuar")

def menu_principal():
        accion = input("\t\t\t..::BIENVENIDO A ADMINISTRADOR DE CALIFICACIONES::..\n\t\#Escpja la accion que quiera realizar\n1.- Agregar calificación\n2.- Mostrar calificacioens\n3.- Calcular promedio de califiaciones\n4.- Salir")

        return accion

def agregar_calificaciones(datos):
    borrarPantalla()
    print("\n..::: AGREGAR CALIFICACIONES :::..\n")
    
    while True:
        opcion = input("¿Agregar nuevo alumno? (si/no): ").lower().strip()
        if opcion != "si" and opcion != "no":
            print("¡Error! Ingrese solo 'si' o 'no'")
            continue
            
        if opcion == 'no':
            return datos
            
        alumno = []
        alumno.append(input("Nombre del alumno: ").upper().strip())
        
        for i in range(3):
            while True:
                try:
                    calif = float(input(f"Calificación {i+1} (0-10): "))
                    if 0 <= calif <= 10:
                        alumno.append(calif)
                        break
                    else:
                        print("¡Error! La calificación debe ser entre 0 y 10")
                except ValueError:
                    print("¡Error! Ingrese un número válido")

        datos.append(alumno)
        print(f"\n¡Alumno {alumno[0]} agregado con éxito!")
        print(f"Calificaciones: {alumno[1:]}")

        try:
            conexion = conectar()
            if conexion:
                cursor = conexion.cursor()
                sql = """INSERT INTO califiaciones 
                          (nombre, califiación_1, calificación_2, califiación_3) 
                          VALUES (%s, %s, %s, %s)"""
                cursor.execute(sql, (alumno[0], alumno[1], alumno[2], alumno[3]))
                conexion.commit()
                print(" Datos guardados en la base de datos")
        except Error as e:
            print(f"Error al guardar: {e}")


        return datos

def mostrar_calificaciones(datos):
        borrarPantalla()
        print("\n..::: MOSTRAR CALIFICACIONES :::..\n")
        print(f"{'nombre':>15}   {'calificación 1':>15}   {'calificación 2':>15}   {'calificación 3':>15}")
        print("-"*70)
        for alumno in datos:
             print(f"{alumno[0]:>15}   {alumno[1]:>15.2f}   {alumno[2]:>15.2f}   {alumno[3]:>15.2f}")
             print("-"*70)
             
def calcular_promedios(datos):
    borrarPantalla()
    print("\n..::: PROMEDIOS DE ALUMNOS :::..\n")
    if len(datos) > 0:
        print(f"{'Nombre':<15} {'Promedio':<10}")
        print("-" * 40)
        promedioGeneral = 0
        for fila in datos:
            promedio = (fila[1] + fila[2] + fila[3]) / 3
            print(f"{fila[0]:<15} {promedio:.2f}")
            promedioGeneral += promedio
        print("-" * 40)
        print(f"Promedio general del grupo: {promedioGeneral / len(datos):.2f}")
    else:
        print("No hay calificaciones existentes")
    esperarTecla()
