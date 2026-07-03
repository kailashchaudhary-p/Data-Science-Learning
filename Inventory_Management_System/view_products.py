import tkinter as tk
from tkinter import ttk

class ViewProducts:
    def __init__(self, parent, db):
        self.db = db
        self.root = tk.Toplevel(parent)
        self.root.title('View Products')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.transient(parent)
        self.root.grab_set()

        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Category', 'Quantity', 'Price', 'Created'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Created', text='Created At')
        self.tree.column('ID', width=60)
        self.tree.column('Name', width=180)
        self.tree.column('Category', width=130)
        self.tree.column('Quantity', width=80)
        self.tree.column('Price', width=100)
        self.tree.column('Created', width=180)
        self.tree.pack(fill='both', expand=True, padx=15, pady=15)

        tk.Button(
            self.root,
            text='Refresh',
            font=('Arial', 11),
            width=14,
            command=self.load_products
        ).pack(pady=10)

        self.load_products()

    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        products = self.db.get_products()
        for product in products:
            self.tree.insert('', tk.END, values=product)
