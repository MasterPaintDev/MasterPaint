import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar, QFileDialog, QColorDialog
from drawing_widget import DrawingWidget

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint App")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawingWidget()
        self.setCentralWidget(self.canvas)

        self.create_menu()
        self.create_toolbar()

    def create_menu(self):
        main_menu = self.menuBar()

        file_menu = main_menu.addMenu("File")
        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Save", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        edit_menu = main_menu.addMenu("Edit")
        color_action = QAction("Choose Color", self)
        color_action.triggered.connect(self.canvas.choose_color)
        edit_menu.addAction(color_action)

        def create_toolbar(self):
            toolbar = self.addToolBar("Tools")

            draw_action = QAction("Draw", self)
            draw_action.triggered.connect(self.canvas.enable_drawing)
            toolbar.addAction(draw_action)

            clear_action = QAction("Clear Canvas", self)
            clear_action.triggered.connect(self.canvas.clear_canvas)
            toolbar.addAction(clear_action)

            color_action = QAction("Choose Color", self)
            color_action.triggered.connect(self.canvas.choose_color)
            toolbar.addAction(color_action)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.canvas.load_image(file_path)

    def save_file(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "", "Images (*.png *.jpg *.bmp)")
        if file_path:
            self.canvas.save_image(file_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec_())
