from .db_connection import get_db_connection


def initialize_database():
    connection = get_db_connection()
    drop_tables(connection)
    create_tables(connection)


def drop_tables(connection):
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS USERS")
    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS USERS(
            id SERIAL PRIMARY KEY,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            );   
        """)
    connection.commit()


if __name__ == "__main__":
    initialize_database()
