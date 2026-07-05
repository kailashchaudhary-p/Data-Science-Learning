import tkinter as tk
from login import Login


class WelcomeScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Welcome')
        self.root.geometry('780x520')
        self.root.resizable(False, False)
        self.root.configure(bg='#f5f5f5')

        tk.Label(
            self.root,
            text='Welcome to Inventory Management System',
            font=('Arial', 24, 'bold'),
            bg='#f5f5f5',
            fg='#1f4e79'
        ).pack(pady=40)

        tk.Label(
            self.root,
            text='Manage products and stock with ease.',
            font=('Arial', 14),
            bg='#f5f5f5'
        ).pack(pady=10)

        tk.Button(
            self.root,
            text='Continue to Login',
            font=('Arial', 12, 'bold'),
            bg='#2e86c1',
            fg='white',
            width=20,
            command=self.open_login
        ).pack(pady=30)

    def open_login(self):
        self.root.destroy()
        app = Login()
        app.run()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = WelcomeScreen()
    app.run()
