from conexionBD import conectar, hash_password, verificar_password
from funciones import opcion, pausa, no_vacio, email as pedir_email, passwd as pedir_pwd

def iniciar_sesion(email, password):
    cn = conectar()
    if not cn: return None
    cur = cn.cursor(dictionary=True)
    cur.execute("SELECT * FROM usuarios WHERE email=%s AND activo=1", (email,))
    u = cur.fetchone()
    cur.close(); cn.close()
    if u and verificar_password(password, u["password_hash"]):
        return (u["id"], u["nombre"], u["apellidos"], u["rol"])
    return None

def validar_admin(email_admin, password_admin):
    cn = conectar()
    if not cn: return False
    cur = cn.cursor(dictionary=True)
    cur.execute("SELECT password_hash FROM usuarios WHERE email=%s AND rol='ADMIN' AND activo=1", (email_admin,))
    u = cur.fetchone()
    cur.close(); cn.close()
    return u and verificar_password(password_admin, u["password_hash"])

def crear_usuario(admin_email, admin_pass):
    if not validar_admin(admin_email, admin_pass):
        print("❌ Clave de administrador inválida."); pausa(); return
    nombre = no_vacio("Nombre: ").title()
    apellidos = no_vacio("Apellidos: ").title()
    correo = pedir_email("Email: ")
    rol = opcion("Rol (ADMIN/PROFESOR/ALUMNO): ", ["ADMIN","PROFESOR","ALUMNO"])
    clave = pedir_pwd("Contraseña: ")
    if opcion("Confirmar creación? (S/N): ", ["S","N"]) == "N":
        print("Cancelado."); pausa(); return
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    try:
        cur.execute("""INSERT INTO usuarios(nombre,apellidos,email,password_hash,rol)
                       VALUES(%s,%s,%s,%s,%s)""",
                    (nombre, apellidos, correo, hash_password(clave), rol))
        cn.commit(); print("✅ Usuario creado.")
    except Exception as e:
        cn.rollback(); print("❌ Error al crear usuario:", e)
    cur.close(); cn.close(); pausa()

def listar_usuarios():
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    cur.execute("SELECT id, nombre, apellidos, email, rol FROM usuarios WHERE activo=1 ORDER BY rol, apellidos, nombre")
    datos = cur.fetchall()
    cur.close(); cn.close()
    if not datos:
        print("No hay usuarios activos.")
    else:
        print("\n{:<4} | {:<22} | {:<30} | {:<18} | {:<9}".format("ID","Nombre","Email","Rol",""))
        print("-"*90)
        for r in datos:
            nom = f"{r[1]} {r[2]}"
            print("{:<4} | {:<22} | {:<30} | {:<18}".format(r[0], nom[:22], r[3][:30], r[4]))
    pausa()
