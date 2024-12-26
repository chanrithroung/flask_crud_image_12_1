import pymysql
from dotenv import load_dotenv
from os import getenv

load_dotenv()

DB_HOST = getenv('DB_HOST')
DB_USER = getenv('DB_USER')
DB_NAME = getenv('DB_NAME')
DB_PASSWORD = getenv('DB_PASSWORD') 

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