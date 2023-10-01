import sqlite3
from abc import ABC, abstractmethod


class IDateBaseAdapter(ABC):
    @abstractmethod
    def insert(self, *args):
        pass
    
    @abstractmethod
    def delete(self, *args):
        pass
    
    @abstractmethod
    def update(self, *args):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
    

class DataBase:
    
    def __init__(self, db_name) -> None:
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()  

    def execute(self, cmd):
        self.cursor.execute(cmd) 
        self.conn.commit()
    
    def get_all(self, sql_cmd):
        self.cursor.execute(sql_cmd)
        rows = self.cursor.fetchall()  
        return rows


class DataBaseAdapter(IDateBaseAdapter):
    def __init__(self, db_address) -> None:
        self.db_address = db_address
        self.table_name = 'Products'
        self.product_name_field = 'ProductName'
        self.category_field = 'CategoryID'
        self.price_field = 'Price'
        self.amount_field = 'Amount'

        self.db = DataBase(self.db_address)
        create_cmd = f"CREATE TABLE IF NOT EXISTS {self.table_name}"\
                     f"(id INTEGER PRIMARY KEY, {self.product_name_field} TEXT UNIQUE, {self.category_field} INTEGER, "\
                     f"{self.amount_field} INTEGER, {self.price_field} INTEGER)"
        self.db.execute(create_cmd)

    def insert(self, product_name, category, price, amount):
        cmd = f"INSERT INTO {self.table_name} VALUES (NULL,'{product_name}',{category},{price},{amount})"
        self.db.execute(cmd)

    def delete(self, product_name):
        cmd = f"DELETE FROM {self.table_name} WHERE {self.product_name_field}={product_name}"
        self.db.execute(cmd)

    def update(self, product_name, category, price, amount):
        cmd = f"UPDATE {self.table_name} SET {self.category_field}={category}, {self.product_name_field}={price}, {self.amount_field}={amount} "\
              f"WHERE {self.product_name_field}={product_name}"

    def get_all(self):
        cmd = f"SELECT * FROM {self.table_name}"
        return self.db.get_all(cmd)