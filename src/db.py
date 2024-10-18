import psycopg2
from psycopg2 import pool
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Verifica si DATABASE_URL está siendo cargada
DATABASE_URL = os.getenv('DATABASE_URL')
print(f'Conectando a la base de datos: {DATABASE_URL}')  # Verificar la URL

# Configuración de la conexión a PostgreSQL con un pool de conexiones
connection_pool = psycopg2.pool.SimpleConnectionPool(
    1, 20, dsn=DATABASE_URL
)

# Función para obtener una conexión
def get_db_connection():
    return connection_pool.getconn()

# Función para liberar la conexión
def release_db_connection(conn):
    connection_pool.putconn(conn)

# Función para cerrar todas las conexiones
def close_db_connections():
    connection_pool.closeall()