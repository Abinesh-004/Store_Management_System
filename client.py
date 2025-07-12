import tkinter as tk



class ShopManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shop Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        # Initialize database
        self.init_database()

