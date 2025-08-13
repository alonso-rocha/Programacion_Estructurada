from conexionBD import conectar
from funciones import opcion, pausa, no_vacio

def crear_sesion():
    grupo_id = no_vacio("ID grupo: ")
    fecha = no_vacio("Fecha (YYYY-MM-DD): ")
    hora_inicio = no_vacio("Hora inicio (HH:MM:SS): ")
    hora_fin = input("Hora fin (HH:MM:SS, opcional): ").strip() or None
    tema = input("Tema (opcional): ").strip() or None
    if opcion("Confirmar creación? (S/N): ", ["S","N"]) == "N":
        print("Cancelado."); pausa(); return
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    try:
        cur.execute("""INSERT INTO sesiones(grupo_id,fecha,hora_inicio,hora_fin,tema)
                       VALUES(%s,%s,%s,%s,%s)""",
                    (grupo_id, fecha, hora_inicio, hora_fin, tema))
        cn.commit(); print("✅ Sesión creada.")
    except Exception as e:
        cn.rollback(); print("❌ Error al crear sesión:", e)
    cur.close(); cn.close(); pausa()

def listar_sesiones():
    grupo_id = no_vacio("ID grupo: ")
    cn = conectar()
    if not cn: return
    cur = cn.cursor()
    cur.execute("""SELECT id, fecha, hora_inicio, hora_fin, tema
                   FROM sesiones WHERE grupo_id=%s ORDER BY fecha, hora_inicio""", (grupo_id,))
    datos = cur.fetchall()
    cur.close(); cn.close()
    if not datos:
        print("No hay sesiones para este grupo.")
    else:
        print("\n{:<4} | {:<10} | {:<8} | {:<8} | {}".format("ID","Fecha","Inicio","Fin","Tema"))
        print("-"*80)
        for r in datos:
            print("{:<4} | {:<10} | {:<8} | {:<8} | {}".format(r[0], str(r[1]), str(r[2]), str(r[3]) if r[3] else "", r[4] or ""))
    pausa()
