import pymysql

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_NAME = "flask_crud_image"
DB_PASSWORD = "24022004"

def db_connect():
    con = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )

    qeury = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

    cursor = con.cursor()
    cursor.execute(qeury)
    cursor.execute(f"USE {DB_NAME}")
    con.commit()

    return con


if __name__ == '__main__':
    db_connect()