"""dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)
pelicula = {
    "nombre": "",
    "categoria": "",
    "clasificacion": "",
    "genero": "",
    "idioma": ""
}
"""

pelicula = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar...\n\t")
    
def crearPeliculas():
    borrarPantalla()
    print("\n\t.:: Alta de Películas ::.\n")
    pelicula.update({"nombre": input("Ingresa el nombre: ").upper().strip()})
#   pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()         #una forma relativa de hacer lo de la linea 23
    pelicula.update({"categoria": input("Ingresa la categoría: ").upper().strip()})
    pelicula.update({"clasificacion": input("Ingresa la clasificación: ").upper().strip()})
    pelicula.update({"genero": input("Ingresa el género: ").upper().strip()})
    pelicula.update({"idioma": input("Ingresa el idioma: ").upper().strip()})
    input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Consultar o Mostrar la Película ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"\t{i}: {pelicula[i]}")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar o Quitar TODAS las caracteristicas ::.\n")
    resp = input("¿Deseas quitar o borrar todas las películas del sistema? (Si/No): ").lower().strip()
    if resp == "si":
        pelicula.clear()
        input("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Agregar Característica a Películas ::.\n")
    atributo = input("Ingresa la nueva característica de la película: ").lower().strip()
    valor = input("Ingresa el valor de la característica de la película: ").upper().strip()
    pelicula.update({atributo:valor})
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Modificar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
            resp=input(f"\n\tDeseas modificar el valor de: {i}? (Si/No)").lower().strip()
            if resp=="si":
                pelicula[i]=input(f"\n\tIngrese el nuevo valor de la caracteristica {i}: ").upper().strip()
                print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    else:
        print("\n\t ..:: No hay películas en el sistema ::. ")

def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.:: Borrar Característica de Películas ::.\n")
    if len(pelicula) > 0:
        print(f"\n\tValores actuales: \n ")
        for i in pelicula:
            print(f"\t{i} : {pelicula[i]}")
        resp = input(f"\n\t¿Deseas borrar una característica?  (Si/No): ").lower().strip()
        if resp == "si":
            peli=input("\n\tQue caracteristica quiere borrar? ")
        try:
            del pelicula[peli]
            print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON ÉXITO! :::")
        except:
            print("\n\t\t:::  La caracteristica no es valida o no existe  :::")
    else:
        print("\t..:: No hay películas en el sistema ::..\n")

