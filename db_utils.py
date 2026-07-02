import sqlite3

def get_user_by_id(user_id):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Vulnerable: SQL injection
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    cursor.execute(query)
    return cursor.fetchall()

def get_product(name):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    # Vulnerable: SQL injection via f-string
    cursor.execute(f"SELECT * FROM products WHERE name = '{name}'")
