from conexionBD import conectar, hash_password

def run():
    cn = conectar()
    if not cn:
        print("Sin conexión a la base."); return
    cur = cn.cursor()
    email = "admin@correo.com"
    pwd = "123"
    try:
        cur.execute("""
            INSERT INTO usuarios (nombre, apellidos, email, password_hash, rol, activo)
            VALUES (%s, %s, %s, %s, 'ADMIN', 1)
            ON DUPLICATE KEY UPDATE
              password_hash=VALUES(password_hash),
              rol='ADMIN',
              activo=1
        """, ("Alonso", "Administrador", email, hash_password(pwd)))
        cn.commit()
        print("✅ Admin listo: admin@correo.com / 123")
    except Exception as e:
        cn.rollback()
        print("❌ No se pudo crear/actualizar el admin:", e)
    finally:
        cur.close(); cn.close()

if __name__ == "__main__":
    run()
