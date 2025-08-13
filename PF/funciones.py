import os, re, getpass

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def pausa():
    input("\nPresiona ENTER para continuar...")

def confirmar(msg):
    while True:
        r = input(f"{msg} (S/N): ").strip().upper()
        if r in ("S","N"): return r == "S"
        print("Responde S o N.")

def opcion(mensaje, opciones):
    v = [str(x).upper() for x in opciones]
    while True:
        op = input(mensaje).strip().upper()
        if op in v: return op
        print("Opción inválida. Elige:", ", ".join(v))

def entero_pos(mensaje):
    while True:
        t = input(mensaje).strip()
        if re.fullmatch(r"\d+", t) and int(t) > 0: return int(t)
        print("Ingresa solo números positivos.")

def no_vacio(mensaje):
    while True:
        t = input(mensaje).strip()
        if t: return t
        print("Este campo es obligatorio.")

def email(mensaje):
    p = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    while True:
        e = input(mensaje).strip().lower()
        if re.match(p, e): return e
        print("Email no válido.")

def passwd(mensaje="Contraseña: "):
    return getpass.getpass(mensaje).strip()

def titulo(txt):
    print("\n" + "═"*70)
    print(f"{txt:<70}")
    print("═"*70)

def menu(txt, items):
    limpiar()
    titulo(txt)
    for k, v in items:
        print(f" {k:<2} | {v:<40}")
    return opcion("Elige: ", [k for k, _ in items])
