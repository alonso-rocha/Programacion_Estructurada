from conexionBD import conectar, hash_password

def crear_admin_si_no_existe():
    cn = conectar()
    if not cn:
        print("No hay conexión."); return
    cur = cn.cursor()
    cur.execute("SELECT COUNT(*) FROM usuarios WHERE rol='ADMIN' AND activo=1")
    hay = cur.fetchone()[0]
    if hay == 0:
        try:
            cur.execute("""INSERT INTO usuarios(nombre, apellidos, email, password_hash, rol, activo)
                           VALUES(%s,%s,%s,%s,'ADMIN',1)""",
                        ("Alonso", "Administrador", "admin@correo.com", hash_password("123")))
            cn.commit()
            print("Admin creado: admin@correo.com / 123")
        except Exception as e:
            cn.rollback()
            print("No se pudo crear el admin:", e)
    else:
        print("Ya existe un administrador.")
    cur.close(); cn.close()

if __name__ == "__main__":
    crear_admin_si_no_existe()
