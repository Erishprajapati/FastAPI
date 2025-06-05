import psycopg2

def create_connection():
    connection = psycopg2.connect(
        dbname = 'Connection'
        user = 'postgres',
        password = '4696',
        host = 'localhost',
        port = 5432
    )
    return connection