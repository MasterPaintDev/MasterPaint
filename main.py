import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu, QVBoxLayout, QHBoxLayout, QPushButton, QWidget, QLabel, QColorDialog, QFileDialog, QMessageBox
from drawing_widget import DrawingWidget

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint App")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawingWidget()
        self.setCentralWidget(self.canvas)

        self.create_actions()
        self.create_menus()
        self.create_toolbars()

    def create_actions(self):
        self.open_action = QAction("Open", self)
        self.open_action.triggered.connect(self.open_file)

        self.save_action = QAction("Save", self)
        self.save_action.triggered.connect(self.save_file)

        self.clear_action = QAction("Clear Canvas", self)
        self.clear_action.triggered.connect(self.canvas.clear_canvas)

        self.choose_color_action = QAction("Choose Color", self)
        self.choose_color_action.triggered.connect(self.choose_color)

        self.exit_action = QAction("Exit", self)
        self.exit_action.triggered.connect(self.confirm_exit)

    def create_menus(self):
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.open_action)
        file_menu.addAction(self.save_action)
        file_menu.addAction(self.exit_action)

        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction(self.clear_action)
        edit_menu.addAction(self.choose_color_action)

    def create_toolbars(self):
        toolbar = self.addToolBar("Tools")

        draw_button = QPushButton("Draw")
        draw_button.clicked.connect(self.canvas.enable_drawing)
        toolbar.addWidget(draw_button)

        clear_button = QPushButton("Clear")
        clear_button.clicked.connect(self.canvas.clear_canvas)
        toolbar.addWidget(clear_button)

        color_button = QPushButton("Choose Color")
        color_button.clicked.connect(self.choose_color)
        toolbar.addWidget(color_button)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.canvas.load_image(file_path)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.canvas.save_image(file_path)

    def confirm_exit(self):
        reply = QMessageBox.question(self, 'Exit', 'Are you sure you want to exit? Any unsaved changes will be lost.',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.close()

    def closeEvent(self, event):
        if self.canvas.isModified():
            reply = QMessageBox.question(self, 'Save Changes', 'Do you want to save your changes?',
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
