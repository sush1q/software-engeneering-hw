import sqlite3


class DataBase:
    
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(             
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY, ProductName TEXT, SupplierID INTEGER, CategoryID INTEGER, QuantityPerUnit INTEGER и UnitPrice INTEGER)") 
        self.conn.commit()  

    def __del__(self):
        self.conn.close()  

    def get_all(self):
        self.cursor.execute('SELECT * FROM Products')
        rows = self.cursor.fetchall()  
        return rows

    def insert(self):
        raise NotImplementedError
    
    def update(self):
        raise NotImplementedError
    
    def delete(self):
        raise NotImplementedError
