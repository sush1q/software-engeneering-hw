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
    
    def get_all(self):
        self.cursor.execute('SELECT * FROM Products')
        rows = self.cursor.fetchall()  
        return rows

    def insert(self, sql_cmd):
        self.execute(sql_cmd)
    
    def update(self, sql_cmd):
        self.execute(sql_cmd)

    def delete(self, sql_cmd):
        self.execute(sql_cmd)


class DataBaseAdapter(IDateBaseAdapter):
    def __init__(self, db_address) -> None:
        self.db_address = db_address
        self.table_name = 'Products'
        self.product_name_field = 'ProductName'
        self.category_field = 'Category'
        self.price_field = 'Price'
        self.amount_field = 'Amount'
        
        self.db = DataBase(self.db_address)
        create_cmd = f"CREATE TABLE IF NOT EXISTS {self.table_name}"\
                     f"(id INTEGER PRIMARY KEY, {self.product_name_field} TEXT, {self.category_field} TEXT, CategoryID INTEGER, "\
                     f"{self.amount_field} INTEGER и {self.price_field} INTEGER)"
        self.db.execute(create_cmd)

    def insert(self, product_name, category, price, amount):
        "INSERT INTO {self.table_name} VALUES (NULL,?,?,?)", (product, price, comment,)"
        raise NotImplementedError
    
    def delete(self, product_name):
        "DELETE FROM {self.table_name} WHERE id=?"
        raise NotImplementedError
    
    def update(self, product_name, category, price, amount):
        "UPDATE {self.table_name} SET product=?, price=? WHERE id=?"
        raise NotImplementedError
    
    def get_all(self):
        "SELECT * FROM {self.table_name}"
        raise NotImplementedError