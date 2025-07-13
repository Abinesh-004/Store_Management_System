import tkinter as tk
from tkinter import messagebox
from backend.auth import login_user
from ui.register_window import open_register
from ui.admin_dashboard import open_admin_dashboard
from ui.salesperson_dashboard import open_salesperson_dashboard

def open_login():
    def attempt_login():
        username = entry_username.get()
        password = entry_password.get()
        success, data = login_user(username, password)
        if success:
            root.destroy()
            if data["role"] == "admin" or data["role"] == "superuser":
                open_admin_dashboard(data)
            else:
                open_salesperson_dashboard(data)
        else:
            messagebox.showerror("Login Failed", data)

    root = tk.Tk()
    root.title("Shop Login")

    tk.Label(root, text="Username").grid(row=0, column=0)
    tk.Label(root, text="Password").grid(row=1, column=0)

    entry_username = tk.Entry(root)
    entry_password = tk.Entry(root, show="*")
    entry_username.grid(row=0, column=1)
    entry_password.grid(row=1, column=1)

    tk.Button(root, text="Login", command=attempt_login).grid(row=2, column=0, columnspan=2)
    tk.Button(root, text="Register", command=lambda: [root.destroy(), open_register()]).grid(row=3, column=0, columnspan=2)

    root.mainloop()
