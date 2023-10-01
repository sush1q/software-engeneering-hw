from database.db_adapter import DataBaseAdapter


class App:
    def __init__(self, db_address) -> None:
        self.db = DataBaseAdapter(db_address)

    def save(self, product_name, category, price, amount):
        self.db.insert(product_name, category, price, amount)

    def delete(self, product_name):
        self.db.delete(product_name)

    def update(self, product_name, category, price, amount):
        self.db.update(product_name, category, price, amount)

    def show_all(self):
        return self.db.get_all()
