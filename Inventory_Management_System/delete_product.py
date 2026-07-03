import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class DeleteProduct:
    def __init__(self, parent, db):
        self.db = db
        self.root = tk.Toplevel(parent)
        self.root.title('Delete Product')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.transient(parent)
        self.root.grab_set()

        self.tree = ttk.Treeview(self.root, columns=('ID', 'Name', 'Category', 'Quantity', 'Price'), show='headings')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Category', text='Category')
        self.tree.heading('Quantity', text='Quantity')
        self.tree.heading('Price', text='Price')
        self.tree.column('ID', width=60)
        self.tree.column('Name', width=220)
        self.tree.column('Category', width=140)
        self.tree.column('Quantity', width=90)
        self.tree.column('Price', width=110)
        self.tree.pack(fill='both', expand=True, padx=15, pady=15)

        tk.Button(
            self.root,
            text='Delete Selected',
            font=('Arial', 11),
            bg='red',
            fg='white',
            width=16,
            command=self.delete_selected
        ).pack(pady=10)

        self.load_products()

    def load_products(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        products = self.db.get_products()
        for product in products:
            self.tree.insert('', tk.END, values=(product[0], product[1], product[2], product[3], product[4]))

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning('Select Product', 'Please select a product to delete.')
            return

        product_id = self.tree.item(selected[0])['values'][0]
        if messagebox.askyesno('Confirm Delete', 'Delete selected product?'):
            if self.db.delete_product(product_id):
                messagebox.showinfo('Deleted', 'Product deleted successfully.')
                self.load_products()
            else:
                messagebox.showerror('Error', 'Unable to delete product.')
