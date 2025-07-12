import tkinter as tk



class ShopManagementSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shop Management System")
        self.root.geometry("1200x800")
        self.root.configure(bg='#f0f0f0')

        # Initialize database
        self.init_database()

        # Current user info
        self.current_user = None
        self.current_role = None
        self.current_store = None

        # Show login screen
        self.show_login()

    def init_database(self):
        """Initialize SQLite database with all necessary tables"""
        self.conn = sqlite3.connect('shop_management.db')
        self.cursor = self.conn.cursor()

