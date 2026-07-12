
from config.conexion import conexion_db

def eliminar_laptop():
    try:
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        
        id_laptop = int(input("Ingrese ID: "))
        
        sql = "DELETE FROM inventario_laptops WHERE id = %s"
        
        cursor_db.execute(sql, (id_laptop,))
        conexion.commit()
        
        
        if cursor_db.rowcount == 0:
            print(f"No se ha encontrado una laptop con el ID {id_laptop}")
        else:
            print(f"Laptop con el ID {id_laptop} eliminada correctamente.")
        
        cursor_db.close()
        conexion.close()
        
    except ValueError:
        print("⚠ Error: El valor ingresado no es válido")
        

    input("Presione Enter para continuar...")