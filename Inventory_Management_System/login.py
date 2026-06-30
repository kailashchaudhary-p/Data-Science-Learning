import tkinter as tk 
from tkinter import messagebox
class login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Inventory Management System")
        self.root.geometry("600x400")
        self.root.resizable(False,False)
        self.root.configure(bg="white")

        self.text_label = tk.Label(self.root, text="Inventory Management System",font=("Arial",20,"bold"))
        self.text_label.pack(pady=20)
        self.username_label = tk.Label(self.root,text="Username",font=("Arial",12))
        self.username_label.pack(pady=10)
        self.

def run(self):
        self.root.mainloop()