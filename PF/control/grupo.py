from conexionBD import conectar
from funciones import opcion, pausa, no_vacio

def crear_grupo():
    clave = no_vacio("Clave: ").upper()
    nombre = no_vacio("Nombre: ").title()
    periodo = input("Periodo (ej. 2025-2): ").strip()
    aula = input("Aula: ").strip().upper()
    if opcion("Confirmar creación? (S/N): ", ["S","N"]) == "N":
        print("Cancelado."); pausa(); return
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    try:
        cur.execute("""INSERT INTO grupos(clave,nombre,periodo,profesor_id,aula)
                       VALUES(%s,%s,%s,NULL,%s)""",
                    (clave, nombre, periodo, aula))
        cn.commit(); print("✅ Grupo creado.")
    except Exception as e:
        cn.rollback(); print("❌ Error al crear grupo:", e)
    cur.close(); cn.close(); pausa()

def listar_grupos():
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    cur.execute("""SELECT g.id, g.clave, g.nombre, g.periodo, g.aula,
                          u.nombre, u.apellidos
                   FROM grupos g LEFT JOIN usuarios u ON u.id=g.profesor_id
                   WHERE g.activo=1 ORDER BY g.nombre""")
    datos = cur.fetchall()
    cur.close(); cn.close()
    if not datos:
        print("No hay grupos.")
    else:
        print("\n{:<4} | {:<10} | {:<30} | {:<8} | {:<6} | {}".format("ID","Clave","Nombre","Periodo","Aula","Profesor"))
        print("-"*100)
        for r in datos:
            prof = f"{r[5] or ''} {r[6] or ''}".strip() or "(sin asignar)"
            print("{:<4} | {:<10} | {:<30} | {:<8} | {:<6} | {}".format(r[0], r[1], r[2][:30], r[3] or "", r[4] or "", prof))
    pausa()
