import tkinter as tk
from .app import *

class DesktopApp(App):
    def __init__(self, db_address) -> None:
        self.app = App(db_address)
        self.tk = tk.Tk()
        self.tk.title('Software-Engeneering-HW')
        # поля
        self.product_name = None
        self.category_id = None
        self.price = None
        self.amount = None
        # кнопки
        self.save_button = None
        self.delete_button = None
        self.update_button = None
        self.show_all_button = None
        
        self._create_entries()
        self._create_buttons()

        # Запускаем главный цикл обработки событий
        self.tk.mainloop()

    def _create_entries(self):
        # Создаем поля ввода
        self.product_name = tk.Entry(self.tk)
        self.category_id = tk.Entry(self.tk)
        self.price = tk.Entry(self.tk)
        self.amount = tk.Entry(self.tk)

        # Отображение полей ввода на форме
        self.product_name.pack(),
        self.category_id.pack(),
        self.price.pack(),
        self.amount.pack()
        
    def _create_buttons(self):
        # Создаем кнопку
        self.save_button = tk.Button(self.tk, text="Сохранить", command=self.save)
        self.delete_button = tk.Button(self.tk, text="Удалить", command=self.delete)
        self.update_button = tk.Button(self.tk, text="Обновить", command=self.update)
        self.show_all_button = tk.Button(self.tk, text="Показать все", command=self.show_all)
        
        self.save_button.pack(),
        self.delete_button.pack(),
        self.update_button.pack(),
        self.show_all_button.pack()

    def save(self):
        return self.app.save(self.product_name.get(), self.category_id.get(), self.price.get(), self.amount.get())

    def delete(self):
        return self.app.delete(self.product_name.get())
    
    def update(self):
        return self.app.update(self.product_name.get(), self.category_id.get(), self.price.get(), self.amount.get())

    def show_all(self):
        print(self.app.show_all())

