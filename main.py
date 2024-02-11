import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from drawing_widget import DrawingWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drawing App")
        self.setGeometry(100, 100, 800, 600)

        self.drawing_widget = DrawingWidget()
        self.setCentralWidget(self.drawing_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
