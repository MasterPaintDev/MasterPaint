import hashlib
import json

class AuthenticationManager:
    def __init__(self):
        self.users = {}
        self.load_users()

    def load_users(self):
        try:
            with open('users.json', 'r') as f:
                self.users = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.users = {}

    def save_users(self):
        with open('users.json', 'w') as f:
            json.dump(self.users, f)

    def register(self, username, password):
        if username in self.users:
            return False  # Usuario ya registrado
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        self.save_users()
        return True  # Registro exitoso

    def login(self, username, password):
        if username not in self.users:
            return False  # Usuario no registrado
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.users[username] == hashed_password
