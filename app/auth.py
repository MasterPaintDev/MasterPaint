import hashlib

class AuthenticationManager:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return False  # Usuario ya registrado
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        return True  # Registro exitoso

    def login(self, username, password):
        if username not in self.users:
            return False  # Usuario no registrado
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return self.users[username] == hashed_password
