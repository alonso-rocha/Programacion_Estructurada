#agenda_contactos = {
#                "RUBEN":   ["1234-5678", "ruben@gmail.com" ],
#                "DANIEL":  [ "9876-5432", "damiel@gmail.com"],
#                "XIMENA":  ["5555-5555", "ximena@gmail.com" ]
#                    }


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Presione una tecla para continuar...")

def menu_principal():
    opcion = input("\n\t📅 ..::: Sistema de Gestión de Agenda de Contactos :::... 📅\n\t\t1️⃣  Agregar contacto\n\t\t2️⃣  Mostrar todos los contactos\n\t\t3️⃣  Buscar contacto por nombre\n\t\t4️⃣  modificar contacto\n\t\t5️⃣  Eliminar contacto\n\t\t6️⃣  Salir\n\nSeleccione una opción (1-6): ").strip()
    return opcion

def agregar_contacto(agenda):
    borrarPantalla()
    print("Agregar Contacto")
    nombre = input("Ingrese el nombre del contacto: ").strip().upper()
    telefono = input("Ingrese el número de teléfono: ").strip()
    email = input("Ingrese el correo electrónico: ").strip()

    if nombre in agenda:
        print(f"El contacto {nombre} ya existe.")
    else:
        agenda[nombre] = [telefono, email]
        print(f"Contacto {nombre} agregado correctamente.")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("Mostrar Contactos")
    if not agenda:
        print("No hay contactos")
    else:
        print(f"{'nombre':<15}{'telefono':<15}{'email':<15}")
        print("-" * 50)
        for nombre, datos in agenda.items():
            print(f"{nombre:<15}{datos[0]:<15}{datos[1]:<15}")
        print("-" * 50)

def buscar_contactos(agenda):
    borrarPantalla()
    print("Buscar Contactos")
    if not agenda:
        print("No hay contactos")
    else:
        nombre=input("Nombre del contacto a buscar: ").upper().strip()
        if nombre in agenda:
            print(f"{'Nombre':<15}{'Teléfono':<15}{'E-mail':<15}")
            print("-" * 50)
            print(f"{nombre:<15}{agenda[nombre][0]:<15}{agenda[nombre][1]:<15}")
            print("-" * 50)
        else:
            print("No existe el contacto")

def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar Contacto")
    if not agenda:
        print("No hay contactos")
    else:
        nombre = input("Ingrese el nombre del contacto a modificar: ").strip().upper()
        if nombre in agenda:
            telefono = input("Ingrese el nuevo número de teléfono: ").strip()
            email = input("Ingrese el nuevo correo electrónico: ").strip()
            agenda[nombre] = [telefono, email]
            print(f"Contacto {nombre} modificado correctamente.")
        else:
            print("No existe el contacto")

def eliminar_contacto(agenda):
    borrarPantalla()
    print("Eliminar Contacto")
    if not agenda:
        print("No hay contactos")
    else:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").strip().upper()
        if nombre in agenda:
            del agenda[nombre]
            print(f"Contacto {nombre} eliminado correctamente.")
        else:
            print("No existe el contacto")
        