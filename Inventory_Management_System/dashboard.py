import tkinter as tk
from add_product import AddProduct
from view_products import ViewProducts
from update_product import UpdateProduct
from delete_product import DeleteProduct
from search_product import SearchProduct

class Dashboard:
    def __init__(self, db):
        self.db = db
        self.root = tk.Tk()
        self.root.title('Inventory Management System')
        self.root.geometry('920x620')
        self.root.resizable(False, False)
        self.root.configure(bg='white')

        title = tk.Label(
            self.root,
            text='Inventory Management System',
            font=('Arial', 24, 'bold'),
            bg='darkblue',
            fg='white'
        )
        title.pack(fill='x')

        welcome = tk.Label(
            self.root,
            text='Welcome Admin',
            font=('Arial', 18),
            bg='white'
        )
        welcome.pack(pady=20)

        button_frame = tk.Frame(self.root, bg='white')
        button_frame.pack(pady=30)

        self.add_button = tk.Button(
            button_frame,
            text='Add Product',
            width=20,
            height=2,
            command=self.open_add_product
        )
        self.add_button.grid(row=0, column=0, padx=15, pady=15)

        self.view_button = tk.Button(
            button_frame,
            text='View Products',
            width=20,
            height=2,
            command=self.open_view_products
        )
        self.view_button.grid(row=0, column=1, padx=15, pady=15)

        self.update_button = tk.Button(
            button_frame,
            text='Update Product',
            width=20,
            height=2,
            command=self.open_update_product
        )
        self.update_button.grid(row=1, column=0, padx=15, pady=15)

        self.delete_button = tk.Button(
            button_frame,
            text='Delete Product',
            width=20,
            height=2,
            command=self.open_delete_product
        )
        self.delete_button.grid(row=1, column=1, padx=15, pady=15)

        self.search_button = tk.Button(
            button_frame,
            text='Search Product',
            width=20,
            height=2,
            command=self.open_search_product
        )
        self.search_button.grid(row=2, column=0, padx=15, pady=15)

        self.logout_button = tk.Button(
            button_frame,
            text='Logout',
            width=20,
            height=2,
            bg='red',
            fg='white',
            command=self.logout
        )
        self.logout_button.grid(row=2, column=1, padx=15, pady=15)

    def open_add_product(self):
        AddProduct(self.root, self.db)

    def open_view_products(self):
        ViewProducts(self.root, self.db)

    def open_update_product(self):
        UpdateProduct(self.root, self.db)

    def open_delete_product(self):
        DeleteProduct(self.root, self.db)

    def open_search_product(self):
        SearchProduct(self.root, self.db)

    def logout(self):
        self.root.destroy()
        from login import Login
        Login().run()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    from database import Database
    Dashboard(Database()).run()
