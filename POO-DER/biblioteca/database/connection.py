import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="biblioteca",
        user="postgres",
        password="tu_password"
    )