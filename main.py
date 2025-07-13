from backend.db_manager import init_db
from ui.login_window import open_login

if __name__ == "__main__":
    init_db()
    open_login()
