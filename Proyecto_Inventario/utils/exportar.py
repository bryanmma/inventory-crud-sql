import csv
import os
from pathlib import Path
from config.conexion import conexion_db
import time
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent


ruta_csv = BASE_DIR.parent / "data" / "inventario_laptops.csv"
ruta_log = BASE_DIR.parent / "data" / "log_sistema.txt"

(BASE_DIR / "data").mkdir(exist_ok=True)

def exportar_csv():
    try:
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        
        sql = "SELECT * FROM inventario_laptops"
        
        cursor_db.execute(sql)
        datos = cursor_db.fetchall()
        
        tiempo = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        # Usamos newline='' para evitar líneas en blanco extra en Windows
        with open(ruta_csv, "w", encoding="utf-8", newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(["ID", "Marca", "Modelo", "Categoria", "Precio", "Cantidad", "Tienda"])
            writer.writerows(datos)
            
        with open(ruta_log, "a", encoding="utf-8") as log:
            log.write(f"Se exportó el archivo CSV de forma correcta | {tiempo}\n")
    
        print(f"Archivo exportado correctamente en: {ruta_csv}")
        
        cursor_db.close()
        conexion.close()

    except Exception as error:
        print(f"Ocurrió un error al exportar: {error}")

    input("Presione Enter para continuar...")