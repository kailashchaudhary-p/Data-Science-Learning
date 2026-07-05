import tkinter as tk
from tkinter import messagebox

class AddProduct:
    def __init__(self, parent, db):
        self.parent = parent
        self.db = db

        self.root = tk.Toplevel(parent)
        self.root.title('Add Product')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.transient(parent)
        self.root.grab_set()

        tk.Label(self.root, text='Product Name', font=('Arial', 12)).pack(pady=6)
        self.product_name = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.product_name.pack(pady=4)

        tk.Label(self.root, text='Category', font=('Arial', 12)).pack(pady=6)
        self.category = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.category.pack(pady=4)

        tk.Label(self.root, text='Quantity', font=('Arial', 12)).pack(pady=6)
        self.quantity = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.quantity.pack(pady=4)

        tk.Label(self.root, text='Price', font=('Arial', 12)).pack(pady=6)
        self.price = tk.Entry(self.root, width=35, font=('Arial', 12))
        self.price.pack(pady=4)

        tk.Button(
            self.root,
            text='Save Product',
            font=('Arial', 12),
            bg='green',
            fg='white',
            width=20,
            command=self.save_product
        ).pack(pady=18)

    def save_product(self):
        name = self.product_name.get().strip()
        category = self.category.get().strip()
        quantity = self.quantity.get().strip()
        price = self.price.get().strip()

        if not name or not quantity or not price:
            messagebox.showerror('Validation Error', 'Name, quantity, and price are required.')
            return

        try:
            quantity_value = int(quantity)
            price_value = float(price)
        except ValueError:
            messagebox.showerror('Validation Error', 'Quantity must be an integer and price must be a number.')
            return

        if quantity_value < 0 or price_value < 0:
            messagebox.showerror('Validation Error', 'Quantity and price must be non-negative.')
            return

        if self.db.add_product(name, category, quantity_value, price_value):
            messagebox.showinfo('Success', 'Product added successfully.')
            self.product_name.delete(0, tk.END)
            self.category.delete(0, tk.END)
            self.quantity.delete(0, tk.END)
            self.price.delete(0, tk.END)
        else:
            messagebox.showerror('Error', 'Unable to save product. Please check the database connection.')
