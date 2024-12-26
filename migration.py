from repository import db_connect
from pymysql import MySQLError

def Product():
    query = """
        CREATE TABLE products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name varchar(100) NOT NULL,
            description TEXT,
            thumbnail varchar(255),
            created_at datetime default current_timestamp
        );"""
    con = db_connect()
    cursor = con.cursor()

    try:
        cursor.execute(query=query)
    except MySQLError as error:
        print(f"Fial to create table because: {error}")

if __name__ == "__main__":
    Product()