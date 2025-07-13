import tkinter as tk
from tkinter import messagebox
from backend.auth import register_user
from ui.login_window import open_login

def open_register():
    def attempt_register():
        username = entry_username.get()
        password = entry_password.get()
        role = role_var.get()

        success, message = register_user(username, password, role)
        if success:
            messagebox.showinfo("Success", message)
            root.destroy()
            open_login()
        else:
            messagebox.showerror("Error", message)

    root = tk.Tk()
    root.title("Register Account")

    tk.Label(root, text="Username").grid(row=0, column=0)
    tk.Label(root, text="Password").grid(row=1, column=0)
    tk.Label(root, text="Role").grid(row=2, column=0)

    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*")
    role_var = tk.StringVar(value="salesperson")
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)
    tk.OptionMenu(root, role_var, "salesperson").grid(row=2, column=1)

    tk.Button(root, text="Register", command=attempt_register).grid(row=3, column=0, columnspan=2)
    root.mainloop()
