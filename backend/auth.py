from backend.db_manager import get_connection
from utils.security import hash_password, verify_password

def register_user(username, password, role):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                    (username, hash_password(password), role))
        conn.commit()
        return True, "Registration successful! Wait for approval."
    except Exception as e:
        return False, str(e)
    finally:
        conn.close()

def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, password, role, is_approved FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    conn.close()
    if result:
        user_id, hashed, role, approved = result
        if not approved and role == "salesperson":
            return False, "Account not approved yet."
        if verify_password(password, hashed):
            return True, {"id": user_id, "username": username, "role": role}
    return False, "Invalid credentials."
