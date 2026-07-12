
from config.conexion import conexion_db

def ver_inventario():
    try:
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        
        num = int(input("Ingrese el número de laptops que desea visualizar: "))
        
        sql = "SELECT * FROM inventario_laptops LIMIT %s"
        cursor_db.execute(sql, (num,))
        
        tabla = cursor_db.fetchall()
        
        for fila_tabla in tabla:
            print(f"{fila_tabla[0]}: {fila_tabla[1]} {fila_tabla[2]} / S/{fila_tabla[4]:,.2f} / {fila_tabla[5]} unidades")


        cursor_db.close()
        conexion.close()
        
    except ValueError:
        print("⚠ Error: El valor ingresado no es válido")
        
    
    input("Enter para continuar...")        
        
    

