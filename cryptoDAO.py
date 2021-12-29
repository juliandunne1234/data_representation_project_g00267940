import mysql.connector

class CryptoDAO:
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarep'
        )

    def create(self, crypto):
        cursor = self.db.cursor()
        sql = "insert into cryptos (id, cryptocurrency, USD_price) values(%s, %s, %s)"
        values = [
            crypto['id'],
            crypto['cryptocurrency'],
            crypto['USD_price']
            ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from cryptos'
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)
        
        return returnArray
    
    def convertToDict(self, result):
        colnames = ['id', 'cryptocurrency', 'USD_price']
        crypto = {}

        if result:
            for i, colname in enumerate(colnames):
                value = result[i]
                crypto[colname] = value
        return crypto

    def findById(self, id):
        cursor = self.db.cursor()
        sql = 'select * from cryptos where id = %s'
        values = [id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result)

    def update(self, crypto):
        cursor = self.db.cursor()
        sql = "update cryptos set cryptocurrency = %s, USD_price = %s where id = %s"
        values = [
            crypto['cryptocurrency'],
            crypto['USD_price'],
            crypto['id']
            ]
        cursor.execute(sql, values)
        self.db.commit()
        return crypto
    
    def delete(self, cryptocurrency):
        cursor = self.db.cursor()
        sql = 'delete from cryptos where cryptocurrency = %s'
        values = [cryptocurrency]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.db.commit()
        return {}

cryptoDAO = CryptoDAO()