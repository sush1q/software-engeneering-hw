import tkinter as tk
from .app import *
from tkinter import messagebox


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
        # лейблы
        self.product_name_label = None
        self.category_id_label = None
        self.price_label = None
        self.price_label = None
        # кнопки
        self.save_button = None
        self.delete_button = None
        self.update_button = None
        self.amount_label = None
        
        self._create_entries()
        self._create_buttons()
        self._init_elements(
            self.product_name_label, self.product_name, 
            self.category_id_label, self.category_id, 
            self.price_label, self.price, 
            self.amount_label, self.amount, 
            self.save_button, 
            self.delete_button, 
            self.update_button, 
            self.show_all_button
        )

        # Запускаем главный цикл обработки событий
        self.tk.mainloop()

    def _create_entries(self):
        # Создаем поля ввода
        self.product_name_label = tk.Label(self.tk, text='Название продукта')
        self.product_name = tk.Entry(self.tk)
        self.category_id_label = tk.Label(self.tk, text='ID категории')
        self.category_id = tk.Entry(self.tk)
        self.price_label = tk.Label(self.tk, text='Стоимость')
        self.price = tk.Entry(self.tk)
        self.amount_label = tk.Label(self.tk, text='Количество')
        self.amount = tk.Entry(self.tk)

    def _create_buttons(self):
        # Создаем кнопку
        self.save_button = tk.Button(self.tk, text="Сохранить", command=self.save)
        self.delete_button = tk.Button(self.tk, text="Удалить", command=self.delete)
        self.update_button = tk.Button(self.tk, text="Обновить", command=self.update)
        self.show_all_button = tk.Button(self.tk, text="Показать все", command=self.show_all)

    def _init_elements(self, *args):
        for element in args:
            element.pack()
            
    def _beautify_data(self, data):
        output = 'Данные в БД:\n'
        for item in data:
            output += f"id: {item[0]}; product: {item[1]}; category: {item[2]}; price: {item[3]}; amount: {item[4]}\n"
        return output

    def save(self):
        product = self.product_name.get()
        result = messagebox.askyesno('Подтверждение операции', message=f'Подтвердите операцию добавления продукта:"{product}" в базу данных')
        if result:
            messagebox.showinfo('Результат', 'Операция подтверждена')
            return self.app.save(self.product_name.get(), self.category_id.get(), self.price.get(), self.amount.get())
        else:
            messagebox.showinfo('Результат', 'Операция отменена')
            

    def delete(self):
        product = self.product_name.get()
        result = messagebox.askyesno('Подтверждение операции', message=f'Подтвердите операцию удаление продукта:"{product}" из базы данных')
        if result:
            messagebox.showinfo('Результат', 'Операция подтверждена')
            return self.app.delete(product)
        else:
            messagebox.showinfo('Результат', 'Операция отменена')
    
    def update(self):
        product = self.product_name.get()
        result = messagebox.askyesno('Подтверждение операции', message=f'Подтвердите операцию обновления данных продукта:"{product}" из базы данных')
        if result:
            messagebox.showinfo('Результат', 'Операция подтверждена')
            return self.app.update(product, self.category_id.get(), self.price.get(), self.amount.get())
        else:
            messagebox.showinfo('Результат', 'Операция отменена')

    def show_all(self):
        data = self._beautify_data(self.app.show_all())
        messagebox.showinfo('Данные в БД', data)

