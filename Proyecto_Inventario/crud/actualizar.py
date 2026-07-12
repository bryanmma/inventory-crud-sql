
from config.conexion import conexion_db

def actualizar_precio():
    try:
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        

        id_laptop = int(input("Ingrese ID: "))
        nuevo_precio = float(input("Nuevo precio: "))
            
        
        sql = "UPDATE inventario_laptops SET precio = %s WHERE id = %s"
        
        cursor_db.execute(sql, (nuevo_precio, id_laptop))
        conexion.commit()
        
        if cursor_db.rowcount == 0:
            print(f"No se ha encontrado laptop con el ID {id_laptop}")
            
        else:
            print(f"Se actualizó la información de la laptop con el ID {id_laptop}")
        
        
        cursor_db.close()
        conexion.close()

        
        
    except ValueError:
        print("⚠ Error: El valor ingresado no es válido")
        

    input("Presione Enter para continuar...")