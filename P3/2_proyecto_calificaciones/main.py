"""
PROYECTO 3
crear un poryecto que perminta administrar peliculas; 
colocar un menu de opciones para gregar, mostrar y calcular el romedio de calificacioens

notas.
1.-Utilizar funciones y mandar a llamar desde otro archivo. 
2.-Utilizar listas para almacenar el nombre y 3 calificaiones de los alumnos.
"""

import os 
os.system("cls")
import calificaciones



def main ():

    opcion = True
    datos = []
    calificaciones.borrarPantalla()
    while opcion == True:
        accion = calificaciones.menu_principal()
        
        
        match accion:
            case "1":
                datos = calificaciones.agregar_calificaciones(datos)
                print(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_promedios(datos) 
            case "4":
                opcion=False    
                calificaciones.borrarPantalla()
                print("Terminaste la ejecucion del SW")
            case _: 
                opcion = True
                input("Opción invalida vuelva a intentarlo ... por favor")



if __name__ == "__main__":
    main()