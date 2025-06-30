"""
Proyecto 1.
Crear un proyecto que permita gestionar (administrar) películas; colocar un menú de opciones para agregar,
eliminar, modificar y consultar películas.
-Notas: 1.-Utilizar funciones y mandar llamar desde otro archivo.
        2.-Utilizar dict para almacenar los siguientes atributos: (nombre, categoría, clasificación,
          genero, idioma) de las peliculas."""

import peliculas

opcion=True
while opcion:
 print ("\n\t.::CINEPOLIS CLON::.\n..:::Sistema de Gestión de Películas:::..\t\t\t\n\n1.-Crear\t\t\n2.-Borrar\t\t\n3.-Mostrar\t\t\n4.-Agregar Caracteristícas\t\t\n5.-Modificar Caracteristícas\t\t\n6.-Borrar Caracteristícas \t\t\n7.-SALIR" )
 opcion=input("\t Elige una opción: ").upper()

 match opcion:#Match: Cadena y enteros (Solo acepta esos dos)
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            peliculas.esperarTecla() 
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()  
        case "4":
            peliculas.agregarCaracteristicaPeliculas() 
            peliculas.esperarTecla()
        case "5": 
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6": 
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False 
            peliculas.borrarPantalla()   
            print("\n\t\tTerminaste la ejecucion del SW")
        case _:#significa que cualquier opcion invalida va a caer aqui 
            opcion=True
            input("\n\t\tOpción invalida vuelva a intentarlo ... por favor")
