import os
import peliculas 

# Crear un proyecto que permita gestionar (administrar) peliculas, colocar un menu de opciones para agregar, eliminar, modificar, consultar, buscar y baciar peliculas.
# Notas 
# 1.- Utilizar funciones y mandar llamar desde otro archivo  
# 2.- Utilizar listas para almacenar los nombres de las peliculas


opcion=True
while opcion:
    print("\n\t\t\t ..::: CINEPOLIS CLON :::.. \n\t\t ..::: Sistema de Gestión de Peliculas :::.. \n\t\t 1.- Agregar \n\t\t 2.- Eliminar \n\t\t 3.- Modificar \n\t\t 4.- Consultar \n\t\t 5.- Buscar \n\t\t 6.- Vaciar \n\t\t 7.- Salir ")

    opcion=input("\n\t\t Elije una opcion: ")

    match opcion:
        case "1":
            peliculas.agragarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas() 
            peliculas.esperarTecla() 
        case "3":
            peliculas.modificarPeliculas() 
            peliculas.esperarTecla()  
        case "4":
            peliculas.consultarPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.vaciarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False 
            peliculas.borrarPantalla()   
            print("\n\t\tTerminaste la ejecucion del SW")
        case _: 
            opciones=True
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")
