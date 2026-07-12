
from config.conexion import conexion_db

def buscar_laptop():
    try:
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        
        id_laptop = int(input("Ingrese el ID: "))
        
        sql = "SELECT * FROM inventario_laptops WHERE id = %s"
        
        cursor_db.execute(sql, (id_laptop,))
        
        tabla = cursor_db.fetchall()
        
        if len(tabla) == 0:
            print(f"No se encontró una laptop con el ID {id_laptop}")
        else:
            for fila in tabla:
                print(f"{fila[0]}: {fila[1]} {fila[2]} / S/{fila[4]:,.2f} / {fila[5]} unidades")
    
        cursor_db.close()
        conexion.close()    

    except ValueError:
        print("⚠ Error: El valor ingresado no es válido")
    
        
    input("Enter para continuar...")