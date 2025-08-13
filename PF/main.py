import sys
from conexionBD import conectar, hash_password
from funciones import limpiar, pausa, menu, opcion, email as pedir_email, passwd as pedir_pwd, confirmar
from usuarios import usuario as U
from control import grupo as G, sesion as S, asistencias as AS

def forzar_admin_rescate():
    cn = conectar()
    if not cn:
        print("Sin conexión a la base."); sys.exit(1)
    cur = cn.cursor()
    cur.execute("""
        INSERT INTO usuarios(nombre, apellidos, email, password_hash, rol, activo)
        VALUES (%s,%s,%s,%s,'ADMIN',1)
        ON DUPLICATE KEY UPDATE
          password_hash=VALUES(password_hash),
          rol='ADMIN',
          activo=1
    """, ("Alonso","Administrador","admin@correo.com",hash_password("123")))
    cn.commit()
    cur.close(); cn.close()

def vista_admin(uid, nombre):
    while True:
        op = menu("MENÚ ADMIN", [("1","Usuarios"),("2","Grupos"),("3","Sesiones"),("4","Asistencias"),("0","Cerrar sesión")])
        if op == "1":
            sub = menu("USUARIOS", [("1","Crear"),("2","Listar"),("0","Regresar")])
            if sub == "1":
                print("\nAutenticación ADMIN")
                aem = pedir_email("Email ADMIN: ")
                apw = pedir_pwd("Contraseña ADMIN: ")
                U.crear_usuario(aem, apw)
            elif sub == "2":
                U.listar_usuarios()

        elif op == "2":
            sub = menu("GRUPOS", [("1","Crear"),("2","Listar"),("3","Asignar profesor"),("0","Regresar")])
            if sub == "1":
                G.crear_grupo()
            elif sub == "2":
                G.listar_grupos()
            elif sub == "3":
                gid = input("ID grupo: ").strip()
                pid = input("ID profesor: ").strip()
                if not gid.isdigit() or not pid.isdigit():
                    print("IDs inválidos."); pausa(); continue
                if not confirmar("¿Asignar profesor?"): print("Cancelado."); pausa(); continue
                cn = conectar()
                if not cn: print("Sin conexión."); pausa(); continue
                cur = cn.cursor()
                try:
                    cur.execute("UPDATE grupos SET profesor_id=%s WHERE id=%s", (int(pid), int(gid)))
                    cn.commit(); print("Profesor asignado.")
                except Exception as e:
                    cn.rollback(); print("No se pudo asignar:", e)
                cur.close(); cn.close(); pausa()

        elif op == "3":
            sub = menu("SESIONES", [("1","Crear"),("2","Ver por grupo"),("0","Regresar")])
            if sub == "1":
                S.crear_sesion()
            elif sub == "2":
                S.listar_sesiones()

        elif op == "4":
            AS.ver_por_sesion()

        elif op == "0":
            break

def vista_profesor(uid, nombre):
    while True:
        op = menu("MENÚ PROFESOR", [("1","Mis grupos"),("2","Sesiones de mi grupo"),("3","Pasar lista"),("0","Cerrar sesión")])
        if op == "1":
            cn = conectar()
            if not cn: print("Sin conexión."); pausa(); continue
            cur = cn.cursor()
            cur.execute("""SELECT id, clave, nombre, periodo, aula
                           FROM grupos WHERE activo=1 AND profesor_id=%s ORDER BY nombre""", (uid,))
            filas = cur.fetchall()
            if not filas:
                print("No tienes grupos asignados.")
            else:
                print("\n{:<4} | {:<10} | {:<30} | {:<8} | {:<6}".format("ID","Clave","Nombre","Periodo","Aula"))
                print("-"*80)
                for r in filas:
                    print("{:<4} | {:<10} | {:<30} | {:<8} | {:<6}".format(r[0], r[1], r[2][:30], r[3] or "", r[4] or ""))
            cur.close(); cn.close(); pausa()

        elif op == "2":
            gid = input("ID de tu grupo: ").strip()
            if not gid.isdigit(): print("ID inválido."); pausa(); continue
            cn = conectar()
            if not cn: print("Sin conexión."); pausa(); continue
            cur = cn.cursor()
            cur.execute("""SELECT id, fecha, hora_inicio, hora_fin, tema
                           FROM sesiones WHERE grupo_id=%s ORDER BY fecha, hora_inicio""", (int(gid),))
            lst = cur.fetchall()
            if not lst:
                print("No hay sesiones para ese grupo.")
            else:
                print("\n{:<4} | {:<10} | {:<8} | {:<8} | {}".format("ID","Fecha","Inicio","Fin","Tema"))
                print("-"*80)
                for r in lst:
                    print("{:<4} | {:<10} | {:<8} | {:<8} | {}".format(r[0], str(r[1]), str(r[2]), str(r[3]) if r[3] else "", r[4] or ""))
            cur.close(); cn.close(); pausa()

        elif op == "3":
            AS.marcar()

        elif op == "0":
            break

def vista_alumno(uid, nombre):
    while True:
        op = menu("MENÚ ALUMNO", [("1","Mis asistencias"),("0","Cerrar sesión")])
        if op == "1":
            AS.ver_mias(uid)
        elif op == "0":
            break

def main():
    forzar_admin_rescate()
    while True:
        op = menu("SISTEMA DE ASISTENCIAS", [("1","Iniciar sesión"),("0","Salir")])
        if op == "1":
            em = pedir_email("Email: ")
            pw = pedir_pwd("Contraseña: ")
            x = U.iniciar_sesion(em, pw)
            if not x:
                print("Email y/o contraseña incorrectos."); pausa(); continue
            uid, nom, ap, rol = x
            print(f"\nBienvenido {nom} {ap}. Rol: {rol}")
            if rol == "ADMIN":
                vista_admin(uid, nom)
            elif rol == "PROFESOR":
                vista_profesor(uid, nom)
            else:
                vista_alumno(uid, nom)
        elif op == "0":
            print("Hasta luego."); break

if __name__ == "__main__":
    main()
