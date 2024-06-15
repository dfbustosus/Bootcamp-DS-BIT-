import os
from dotenv import load_dotenv
import psycopg2
from psycopg2 import sql

# cargar variables de entorno .env 
load_dotenv()

# Conectar a la base de datos
def connect_to_db():
    try:
        connection = psycopg2.connect(
            dbname="tienda",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host="localhost",
            port="5432"
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        return None
    
# Ejecución de consultas de ejemplo
def execute_queries(connection):
    try:
        cursor = connection.cursor()
        
        # Consultar todos los clientes
        cursor.execute("SELECT * FROM clientes;")
        clientes = cursor.fetchall()
        print("Clientes:")
        for cliente in clientes:
            print(cliente)
        
        # Consultar todos los productos
        cursor.execute("SELECT * FROM productos;")
        productos = cursor.fetchall()
        print("\nProductos:")
        for producto in productos:
            print(producto)
        
        # Consultar todos los pedidos
        cursor.execute("SELECT * FROM pedidos;")
        pedidos = cursor.fetchall()
        print("\nPedidos:")
        for pedido in pedidos:
            print(pedido)
        
        # Ejemplo de consulta específica
        cursor.execute("""
        SELECT c.nombre, p.nombre, pe.cantidad, pe.fecha_pedido
        FROM pedidos pe
        JOIN clientes c ON pe.cliente_id = c.cliente_id
        JOIN productos p ON pe.producto_id = p.producto_id;
        """)
        resultado = cursor.fetchall()
        print("\nDetalles de pedidos:")
        for row in resultado:
            print(row)
        
    except Exception as error:
        print(f"Error al ejecutar consultas: {error}")

def main():
    connection = connect_to_db()
    if connection:
        execute_queries(connection)
        connection.close()

if __name__ == "__main__":
    main()