"""
Intentionally vulnerable Python code for SAST testing.

⚠️ This file is for testing static analysis tools only.
Do NOT deploy or use in production.
"""

import os
import sqlite3
import pickle
import hashlib
from flask import Flask

# ---------------------------------------------------------------------
# Hardcoded Secret
# ---------------------------------------------------------------------
API_KEY = "1234567890abcdef1234567890abcdef"
DB_PASSWORD = "SuperSecretPassword123!"
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"


# ---------------------------------------------------------------------
# SQL Injection
# ---------------------------------------------------------------------
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Vulnerable: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    return cursor.fetchall()


# ---------------------------------------------------------------------
# Command Injection
# ---------------------------------------------------------------------
def ping(host):
    # Vulnerable: Command Injection
    os.system("ping -c 4 " + host)


# ---------------------------------------------------------------------
# Insecure Deserialization
# ---------------------------------------------------------------------
def load_data(data):
    # Vulnerable: Unsafe deserialization
    return pickle.loads(data)


# ---------------------------------------------------------------------
# Weak Hash Algorithm
# ---------------------------------------------------------------------
def hash_password(password):
    # Vulnerable: Weak cryptographic algorithm
    return hashlib.md5(password.encode()).hexdigest()


# ---------------------------------------------------------------------
# Path Traversal
# ---------------------------------------------------------------------
def read_file(filename):
    # Vulnerable: Path Traversal
    with open("data/" + filename, "r") as f:
        return f.read()


# ---------------------------------------------------------------------
# Dangerous eval()
# ---------------------------------------------------------------------
def calculate(expression):
    # Vulnerable: Arbitrary code execution
    return eval(expression)


# ---------------------------------------------------------------------
# Dangerous exec()
# ---------------------------------------------------------------------
def execute(code):
    # Vulnerable: Arbitrary code execution
    exec(code)


# ---------------------------------------------------------------------
# Insecure Temporary File
# ---------------------------------------------------------------------
def create_temp():
    # Vulnerable: Predictable temporary filename
    with open("/tmp/mytempfile.txt", "w") as f:
        f.write("temporary data")


# ---------------------------------------------------------------------
# Insecure Randomness
# ---------------------------------------------------------------------
import random

def generate_token():
    # Vulnerable: Not cryptographically secure
    return str(random.randint(100000, 999999))


# ---------------------------------------------------------------------
# Flask Debug Mode Enabled
# ---------------------------------------------------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"


# ---------------------------------------------------------------------
# Assertions Used for Security
# ---------------------------------------------------------------------
def authenticate(user):
    # Vulnerable: assert statements can be disabled
    assert user == "admin"
    return True


# ---------------------------------------------------------------------
# Hardcoded Cryptographic Key
# ---------------------------------------------------------------------
AES_KEY = b"0123456789abcdef"


# ---------------------------------------------------------------------
# Insecure File Permissions
# ---------------------------------------------------------------------
def create_world_writable():
    filename = "public.txt"
    with open(filename, "w") as f:
        f.write("hello")

    os.chmod(filename, 0o777)


# ---------------------------------------------------------------------
# Unsafe YAML Loading (requires PyYAML)
# ---------------------------------------------------------------------
try:
    import yaml

    def parse_yaml(data):
        # Vulnerable: Unsafe YAML deserialization
        return yaml.load(data, Loader=yaml.Loader)
except ImportError:
    pass


# ---------------------------------------------------------------------
# Weak SSL Configuration
# ---------------------------------------------------------------------
import ssl

def insecure_ssl_context():
    # Vulnerable: Certificate verification disabled
    ctx = ssl._create_unverified_context()
    return ctx


# ---------------------------------------------------------------------
# Shell=True
# ---------------------------------------------------------------------
import subprocess

def run_command(cmd):
    # Vulnerable: shell=True
    subprocess.call(cmd, shell=True)


# ---------------------------------------------------------------------
# Arbitrary File Write
# ---------------------------------------------------------------------
def write_file(path, content):
    # Vulnerable: User-controlled file path
    with open(path, "w") as f:
        f.write(content)


# ---------------------------------------------------------------------
# Insecure HTTP Request
# ---------------------------------------------------------------------
try:
    import requests

    def download(url):
        # Vulnerable: SSL verification disabled
        return requests.get(url, verify=False)
except ImportError:
    pass


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
