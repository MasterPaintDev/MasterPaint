import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QPushButton, QWidget, QColorDialog, QFileDialog, QMessageBox, QTextEdit, QTabWidget, QLineEdit, QHBoxLayout
from PyQt5.QtCore import QFile
import yaml
import requests
from app.drawing_widget import DrawingWidget
import time

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MasterPaint")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawingWidget()
        self.setCentralWidget(self.canvas)

        self.language = "en"  # Idioma por defecto
        self.load_language()

        self.create_actions()
        self.create_menus()
        self.create_toolbars()
        self.create_updates_tab()

        self.current_version = "v1.0"
        self.check_for_updates()

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
            "ru": "messages-ru.yml"
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

        self.exit_action = QAction(self.messages['actions']['exit'], self)
        self.exit_action.triggered.connect(self.confirm_exit)

        self.show_updates_action = QAction(self.messages['actions']['show_updates'], self)
        self.show_updates_action.triggered.connect(self.show_updates)

        self.language_en_action = QAction("English", self)
        self.language_en_action.triggered.connect(lambda: self.change_language("en"))

        self.language_es_action = QAction("Spanish", self)
        self.language_es_action.triggered.connect(lambda: self.change_language("es"))

        self.language_jp_action = QAction("Japanese", self)
        self.language_jp_action.triggered.connect(lambda: self.change_language("jp"))

        self.language_ru_action = QAction("Russian", self)
        self.language_ru_action.triggered.connect(lambda: self.change_language("ru"))

    def create_menus(self):
        self.menuBar().clear()

        file_menu = self.menuBar().addMenu(self.messages['menus']['file'])
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)

        updates_menu = self.menuBar().addMenu(self.messages['menus']['updates'])
        updates_menu.addAction(self.show_updates_action)

        language_menu = self.menuBar().addMenu(self.messages['menus']['language'])
        language_menu.addAction(self.language_en_action)
        language_menu.addAction(self.language_es_action)
        language_menu.addAction(self.language_jp_action)
        language_menu.addAction(self.language_ru_action)

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
        self.update_buttons_text()  # Actualizar solo el texto de los botones
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
