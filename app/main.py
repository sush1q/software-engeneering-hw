from db_adapter import *


if __name__ == '__main__':
    db = DataBase('hw-db.db')
    rows = db.get_all()
