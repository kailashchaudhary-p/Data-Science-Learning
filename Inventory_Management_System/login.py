import tkinter as tk 
from tkinter import messagebox
class Login:
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
        self.username=tk.Entry(self.root,font=("Arial",12))
        self.username.pack(pady=10)
        self.password_label = tk.Label(self.root,text="Password",font=("Arial",12))
        self.password_label.pack(pady=10)
        self.password=tk.Entry(self.root,font=("Arial",12),show="*")
        self.password.pack(pady=10)
        self.Login_button = tk.Button(self.root,text="Login",font=("Arial",12),bg="blue",fg="white")
        self.Login_button.pack(pady=30)
        self.Login_button.config(command=self.Login)
        self.exit_button = tk.Button(self.root, text="Exit", font=("Arial",12), bg="red", fg="white", command=self.root.destroy)
        self.exit_button.pack(pady=10)

    def Login(self):
        username = self.username.get()
        password = self.password.get()

        if username == "" or password == "":
              messagebox.showerror("Error", "Please enter username and password")
        else:
              messagebox.showinfo("Success", "Login Successful")


    def run(self):
         self.root.mainloop()
if __name__ == "__main__":
    app = Login()
    app.run()