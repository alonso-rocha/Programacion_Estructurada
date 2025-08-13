from conexionBD import conectar
from funciones import pausa, opcion
from exportacion import exportar_excel

def marcar():
    sid = input("ID de la sesión: ").strip()
    if not sid.isdigit():
        print("ID inválido."); pausa(); return
    print("Estados: A=Asistió, T=Tarde, J=Justificado, F=Falta")
    while True:
        linea = input("ID_alumno,ESTADO (ENTER termina, ej. 12,A): ").strip()
        if not linea: break
        try:
            aid_s, est = [x.strip() for x in linea.split(",")]
            if not aid_s.isdigit() or est not in ("A","T","J","F"):
                print("Formato inválido. Usa 12,A con A/T/J/F."); continue
            obs = input("Observaciones (opcional): ").strip() or None
            cn = conectar()
            if not cn: print("Sin conexión."); continue
            cur = cn.cursor()
            try:
                cur.execute("""INSERT INTO asistencias(sesion_id, alumno_id, estado, observaciones)
                               VALUES(%s,%s,%s,%s)
                               ON DUPLICATE KEY UPDATE estado=VALUES(estado), observaciones=VALUES(observaciones)""",
                            (int(sid), int(aid_s), est, obs))
                cn.commit(); print("Guardado.")
            except Exception as e:
                cn.rollback(); print("No se pudo guardar:", e)
            cur.close(); cn.close()
        except:
            print("Formato inválido.")
    pausa()

def _por_sesion(sid):
    cn = conectar()
    if not cn: print("Sin conexión."); return []
    cur = cn.cursor()
    cur.execute("""SELECT u.id, u.nombre, u.apellidos, a.estado, a.observaciones
                   FROM asistencias a
                   JOIN usuarios u ON u.id=a.alumno_id
                   WHERE a.sesion_id=%s
                   ORDER BY u.apellidos, u.nombre""", (sid,))
    datos = cur.fetchall()
    cur.close(); cn.close()
    return datos

def ver_por_sesion():
    sid = input("ID de la sesión: ").strip()
    if not sid.isdigit():
        print("ID inválido."); pausa(); return
    datos = _por_sesion(int(sid))
    if not datos:
        print("No hay asistencias para esta sesión."); pausa(); return
    print("\n{:<6} | {:<22} | {:<10} | {}".format("ID","Alumno","Estado","Observaciones"))
    print("-"*80)
    for r in datos:
        nom = f"{r[2]} {r[1]}"
        print("{:<6} | {:<22} | {:<10} | {}".format(r[0], nom[:22], r[3], r[4] or ""))
    a = opcion("\n¿Exportar a Excel? (S/N): ", ["S","N"])
    if a == "S":
        ruta = exportar_excel(f"asistencia_sesion_{sid}",
                              ["ID","Nombre","Apellidos","Estado","Observaciones"],
                              datos)
        print("Archivo:", ruta)
    pausa()

def _de_alumno(uid):
    cn = conectar()
    if not cn: print("Sin conexión."); return []
    cur = cn.cursor()
    cur.execute("""SELECT s.id, s.fecha, s.hora_inicio, g.nombre, a.estado
                   FROM asistencias a
                   JOIN sesiones s ON s.id=a.sesion_id
                   JOIN grupos g ON g.id=s.grupo_id
                   WHERE a.alumno_id=%s
                   ORDER BY s.fecha DESC, s.hora_inicio DESC""", (uid,))
    datos = cur.fetchall()
    cur.close(); cn.close()
    return datos

def ver_mias(uid):
    datos = _de_alumno(uid)
    if not datos:
        print("No tienes asistencias registradas."); pausa(); return
    print("\n{:<6} | {:<10} | {:<8} | {:<30} | {:<1}".format("Sesión","Fecha","Inicio","Grupo","E"))
    print("-"*90)
    for r in datos:
        print("{:<6} | {:<10} | {:<8} | {:<30} | {:<1}".format(r[0], str(r[1]), str(r[2]), r[3][:30], r[4]))
    a = opcion("\n¿Exportar a Excel? (S/N): ", ["S","N"])
    if a == "S":
        ruta = exportar_excel("mis_asistencias",
                              ["Sesion","Fecha","Inicio","Grupo","Estado"],
                              datos)
        print("Archivo:", ruta)
    pausa()
