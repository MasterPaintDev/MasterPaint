import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget
from drawing_widget import DrawingWidget

class PaintApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Paint App")
        self.setGeometry(100, 100, 800, 600)

        self.canvas = DrawingWidget()
        self.clear_button = QPushButton("Clear Canvas")
        self.clear_button.clicked.connect(self.canvas.clear_canvas)  # Conecta al método clear_canvas

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.clear_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaintApp()
    window.show()
    sys.exit(app.exec_())
