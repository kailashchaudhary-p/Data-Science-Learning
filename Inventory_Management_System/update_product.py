import tkinter as tk
from tkinter import messagebox

class UpdateProduct:
    def __init__(self, parent, db):
        self.db = db
        self.root = tk.Toplevel(parent)
        self.root.title('Update Product')
        self.root.geometry('440x520')
        self.root.resizable(False, False)
        self.root.transient(parent)
        self.root.grab_set()

        tk.Label(self.root, text='Product ID', font=('Arial', 12)).pack(pady=6)
        self.product_id = tk.Entry(self.root, width=30, font=('Arial', 12))
        self.product_id.pack(pady=4)

        tk.Button(
            self.root,
            text='Load Product',
            font=('Arial', 12),
            bg='blue',
            fg='white',
            width=18,
            command=self.load_product
        ).pack(pady=12)

        tk.Label(self.root, text='Name', font=('Arial', 12)).pack(pady=6)
        self.name = tk.Entry(self.root, width=34, font=('Arial', 12))
        self.name.pack(pady=4)

        tk.Label(self.root, text='Category', font=('Arial', 12)).pack(pady=6)
        self.category = tk.Entry(self.root, width=34, font=('Arial', 12))
        self.category.pack(pady=4)

        tk.Label(self.root, text='Quantity', font=('Arial', 12)).pack(pady=6)
        self.quantity = tk.Entry(self.root, width=34, font=('Arial', 12))
        self.quantity.pack(pady=4)

        tk.Label(self.root, text='Price', font=('Arial', 12)).pack(pady=6)
        self.price = tk.Entry(self.root, width=34, font=('Arial', 12))
        self.price.pack(pady=4)

        tk.Button(
            self.root,
            text='Update Product',
            font=('Arial', 12),
            bg='green',
            fg='white',
            width=18,
            command=self.update_product
        ).pack(pady=18)

    def load_product(self):
        product_id = self.product_id.get().strip()
        if not product_id.isdigit():
            messagebox.showerror('Validation Error', 'Enter a valid product ID.')
            return

        product = self.db.get_product_by_id(int(product_id))
        if not product:
            messagebox.showerror('Not Found', 'Product not found.')
            return

        _, name, category, quantity, price = product
        self.name.delete(0, tk.END)
        self.name.insert(0, name)
        self.category.delete(0, tk.END)
        self.category.insert(0, category)
        self.quantity.delete(0, tk.END)
        self.quantity.insert(0, quantity)
        self.price.delete(0, tk.END)
        self.price.insert(0, price)

    def update_product(self):
        product_id = self.product_id.get().strip()
        name = self.name.get().strip()
        category = self.category.get().strip()
        quantity = self.quantity.get().strip()
        price = self.price.get().strip()

        if not product_id.isdigit() or not name or not quantity or not price:
            messagebox.showerror('Validation Error', 'All fields are required and ID must be numeric.')
            return

        try:
            quantity_value = int(quantity)
            price_value = float(price)
        except ValueError:
            messagebox.showerror('Validation Error', 'Quantity must be an integer and price must be numeric.')
            return

        updated = self.db.update_product(int(product_id), name, category, quantity_value, price_value)
        if updated:
            messagebox.showinfo('Success', 'Product updated successfully.')
        else:
            messagebox.showerror('Error', 'Unable to update product.')
