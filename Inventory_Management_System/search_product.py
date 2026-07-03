import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class SearchProduct:
    def __init__(self, parent, db):
        self.db = db
        self.root = tk.Toplevel(parent)
        self.root.title('Search Product')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.transient(parent)
        self.root.grab_set()

        search_frame = tk.Frame(self.root)
        search_frame.pack(pady=15)

        tk.Label(search_frame, text='Search term:', font=('Arial', 12)).pack(side='left', padx=(0, 10))
        self.search_text = tk.Entry(search_frame, width=28, font=('Arial', 12))
        self.search_text.pack(side='left')

        tk.Button(
            search_frame,
            text='Search',
            font=('Arial', 11),
            bg='blue',
            fg='white',
            command=self.search_products
        ).pack(side='left', padx=10)

        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Category', 'Quantity', 'Price', 'Created'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.heading('Created', text='Created At')
        self.tree.column('ID', width=60)
        self.tree.column('Name', width=180)
        self.tree.column('Category', width=140)
        self.tree.column('Quantity', width=90)
        self.tree.column('Price', width=100)
        self.tree.column('Created', width=160)
        self.tree.pack(fill='both', expand=True, padx=15, pady=15)

    def search_products(self):
        term = self.search_text.get().strip()
        if not term:
            messagebox.showwarning('Search', 'Enter a search term.')
            return

        results = self.db.search_products(term)
        for row in self.tree.get_children():
            self.tree.delete(row)

        for product in results:
            self.tree.insert('', tk.END, values=product)
