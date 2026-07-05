import tkinter as tk
from tkinter import messagebox
from database import Database

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Inventory Management System')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.configure(bg='white')

        self.db = Database()
        if not self.db.connected:
            messagebox.showerror(
                'Database Error',
                'Cannot connect to the database. Please check the MySQL server and credentials.'
            )
            self.root.destroy()
            return

        tk.Label(self.root, text='Inventory Management System', font=('Arial', 22, 'bold'), bg='white').pack(pady=20)

        tk.Label(self.root, text='Username', font=('Arial', 12), bg='white').pack(pady=5)
        self.username = tk.Entry(self.root, font=('Arial', 12), width=30)
        self.username.pack(pady=5)

        tk.Label(self.root, text='Password', font=('Arial', 12), bg='white').pack(pady=5)
        self.password = tk.Entry(self.root, font=('Arial', 12), show='*', width=30)
        self.password.pack(pady=5)

        self.login_button = tk.Button(
            self.root,
            text='Login',
            font=('Arial', 12),
            bg='blue',
            fg='white',
            width=20,
            command=self.login
        )
        self.login_button.pack(pady=18)

        self.exit_button = tk.Button(
            self.root,
            text='Exit',
            font=('Arial', 12),
            bg='red',
            fg='white',
            width=20,
            command=self.root.destroy
        )
        self.exit_button.pack()

    def login(self):
        username = self.username.get().strip()
        password = self.password.get().strip()

        if not username or not password:
            messagebox.showerror('Error', 'Please enter username and password')
            return

        if self.db.check_login(username, password):
            messagebox.showinfo('Success', 'Login successful')
            self.root.destroy()
            from dashboard import Dashboard
            Dashboard(self.db).run()
        else:
            messagebox.showerror('Error', 'Invalid username or password')

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    Login().run()
