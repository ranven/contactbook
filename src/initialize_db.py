from db_connection import get_db_connection


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("DROP TABLE IF EXISTS contacts")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            );  
        """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            if SERIAL PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            role TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
            );
        """)
    connection.commit()


def initialize_database():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
