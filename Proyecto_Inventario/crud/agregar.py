
from config.conexion import conexion_db

def agregar_laptop():
    
    try: 
        conexion = conexion_db()
        cursor_db = conexion.cursor()
        
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio (S/): "))
        cantidad = int(input("Cantidad: "))
        tienda = input("Tienda: ")
        
        
        sql = """
        INSERT INTO inventario_laptops (marca, modelo, categoria, precio, cantidad, tienda)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cursor_db.execute(sql, (marca, modelo, categoria, precio, cantidad, tienda))
        conexion.commit()
        
        
        cursor_db.close()
        conexion.close()
        
        print(f"Laptop {marca} {modelo} agregada correctamente.")
        
    except ValueError:
        print("⚠ Error: El valor ingresado no es válido")

    input("Presione Enter para continuar...")