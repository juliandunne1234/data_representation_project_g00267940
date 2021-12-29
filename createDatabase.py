import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE datarep")

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'datarep'
)

cursor = db.cursor()
sql = "CREATE TABLE cryptos (id  VARCHAR(255), cryptocurrency VARCHAR(255), USD_price FLOAT)"

cursor.execute(sql)