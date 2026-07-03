import hashlib
import os

# Hardcoded secret
SECRET_KEY = "hardcoded-jwt-secret-do-not-use"

def hash_password(pwd):
    # Weak hash: MD5
    return hashlib.md5(pwd.encode()).hexdigest()

def authenticate(username, password):
    conn = __import__('sqlite3').connect("users.db")
    # SQL injection
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    conn.execute(query)

def run_admin(cmd):
    # Command injection
    os.system("sudo " + cmd)
