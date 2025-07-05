# Instrucciones
#
#
#
#
__name__ = "__name__"

import calificaciones

def main():
    opcion=True
    datos=[]
    
    while opcion:
        calificaciones.borrarPantalla()
        opcion=calificaciones.menu_principal()

        match opcion:
            case "1":
                calificaciones.agregar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "2":
                calificaciones.mostrar_calificaciones(datos)
                calificaciones.esperarTecla()
            case "3":
                calificaciones.calcular_calificaciones(datos)
                calificaciones.esperarTecla()
            case "4":
                opcion=False
                calificaciones.borrarPantalla()
                print(" Terminando la ejecucion del SW")
            case _:
                opcion=True
                print("Opcion invalida vuelva a intentarlo")
                calificaciones.esperarTecla()

if __name__ == "__name__":
    main()
