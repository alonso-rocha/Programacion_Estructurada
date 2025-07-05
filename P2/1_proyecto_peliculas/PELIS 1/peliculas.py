peliculas = {}

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\tOprima cualquier tecla para continuar ... ")
    borrarPantalla()
    
def agragarPeliculas():
    borrarPantalla()
    print("\n\t\t.::Agregar Películas::. \n")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())#Strip es una función de manejo de cadenas que quita espacios al inicio y al final.
    print("\n\t:::¡LA OPERACIÓN SE REALIZÓ CON EXÍTO!::: \n") 

def consultarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: Consultar o Mostarar TODAS las peliculas ::. \n")
    if len(peliculas)>0:
        for i in range(0,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")
    else:
        print("\n\t.:: No hay peliculas en el sistema ::. \n")

def vaciarPeliculas():
    borrarPantalla()
    print("\n\t\t.:: Limpiar o Borrar TODAS las peliclas ::. \n")
    resp=input("¿Deseas borrar todas las peliculas? (Si/No) \n").upper().strip()
    if resp=="SI":
        peliculas.clear()
        print("\n\t::: ¡LA OPERACIÓN SE REALIZO CON EXITO! :::\n")

def buscarPeliculas():
    borrarPantalla()
    print("\n\t\t.::: ¡Buscar una pelicula! :::. \n")
    pelicula_buscar=input("\n\t Ingresa el nombre de la pelicula a buscar: \n").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t::: no hay ninguna pelicula con este nombre :::\n")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                print(f"\n\tLa pelicula {pelicula_buscar} si la tenemos y esta en el casillero: {i+1} ")
                encontro+=1
        print(f"\n\tTenemos {encontro} pelicla(s) con este titulo")

def modificarPeliculas():
    borrarPantalla()
    print("\n\t\t.::: ¡Modificar una pelicula! :::. \n")
    pelicula_buscar=input("\n\t Ingresa el nombre de la pelicula a buscar: \n").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t::: no hay ninguna pelicula con este nombre :::\n")
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if pelicula_buscar == peliculas[i]:
                resp=input("\n\t¿Deseas modificar la pelicula? (Si/No)").lower().strip()
                if resp == "si":
                    peliculas[i]=input("\n\tIntroduzca el nuevo valor de la pelicula: ").upper().strip()
                    print(f"\n\tLa pelicula ahora se llama {peliculas[i]} y la tenemos en el casillero: {i+1} ")
                    encontro+=1
                    esperarTecla()
        print(f"\n\tSe actualizaron {encontro} pelicla(s) con este titulo")

def borrarPeliculas():
    borrarPantalla()
    print("\n\t\t.::: ¡Borrar una pelicula! :::. \n")
    pelicula_buscar=input("\n\t Ingresa el nombre de la pelicula a borrar: \n").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t::: no se encontro ninguna pelicula con este nombre :::\n")
    else:
        encontro=0
        i = 0
        while  i < len(peliculas):
            if pelicula_buscar == peliculas[i]:
                resp=input("\n\t¿Deseas quitar o borrar la pelicula del sistema? (Si/No)").lower().strip()
                if resp == "si":
                    print(f"\n\tLa pelicula que se borro es: {peliculas[i]} y la tenemos en la casilla: {i+1} ")
                    peliculas.pop(i)
                    print("\n\t::: ¡LA OPERACIÓN SE REALIZO CON EXITO! :::\n")
                    encontro+=1
                    esperarTecla()
                else:
                    i += 1 
        print(f"\n\tSe borro {encontro} pelicla(s) con este titulo")
        esperarTecla()

def agregarCaracteristicasPeliculas ():
    borrarPantalla()
    print("\n\t\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    atributo=input("Ingrese el nombre de la nueva caracteristica: ").lower().strip()
    valor_atributo=input("Ingrese el valor de la nueva caracteristica: ").upper().strip()
    peliculas.update({atributo:valor_atributo})
    print("\n\t::: ¡LA OPERACIÓN SE REALIZÓ CON EXÍTO! :::")
    

