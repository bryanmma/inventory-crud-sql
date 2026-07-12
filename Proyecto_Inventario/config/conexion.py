from config.configuracion import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
import mysql.connector

def conexion_db():
    try:
        conexion = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,        
            database="gestion_productos_db"
        )
        return conexion
    except mysql.connector.Error as err:
        print(f"Error de conexión: {err}")
        return None
    
