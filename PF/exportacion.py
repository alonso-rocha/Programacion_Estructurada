import os
import pandas as pd

BASE = os.path.abspath(os.path.join(os.getcwd(), "exportaciones"))
os.makedirs(BASE, exist_ok=True)

def exportar_excel(nombre, columnas, filas):
    ruta = os.path.join(BASE, f"{nombre}.xlsx")
    df = pd.DataFrame(filas, columns=columnas)
    with pd.ExcelWriter(ruta, engine="openpyxl") as w:
        df.to_excel(w, index=False)
    return ruta
