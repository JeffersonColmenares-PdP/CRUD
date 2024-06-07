# configuracion de la conexion a la DB
import psycopg2

# informacion de mi DB
DATABASE = {
    'dbname': 'Inventario',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',
    'port': 5432
}

# metodo para iniciar la conexion
def get_db():
    return psycopg2.connect(
        dbname=DATABASE['dbname'],
        user=DATABASE['user'],
        password=DATABASE['password'],
        host=DATABASE['host'],
        port=DATABASE['port']
    )

# cerrar la conexion a DB
def close_db(conn):
    conn.close()