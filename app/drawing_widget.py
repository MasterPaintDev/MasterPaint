from PyQt5.QtWidgets import QWidget, QVBoxLayout, QToolBar, QAction, QColorDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint, QRect

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.last_point = QPoint()
        self.drawing = False
        self.lines = []
        self.pen_color = Qt.black
        self.loaded_image = None

        self.create_toolbar()

    def create_toolbar(self):
        toolbar = QToolBar()
        toolbar.setOrientation(Qt.Vertical)
        
        draw_action = QAction("", self)
        draw_action.triggered.connect(self.enable_drawing)
        toolbar.addAction(draw_action)

        clear_action = QAction("", self)
        clear_action.triggered.connect(self.clear_canvas)
        toolbar.addAction(clear_action)

        color_action = QAction("", self)
        color_action.triggered.connect(self.choose_color)
        toolbar.addAction(color_action)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen_color = color
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.pen_color, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

        if self.loaded_image:
            painter.drawPixmap(self.rect(), self.loaded_image)

        for line in self.lines:
            painter.drawLine(*line)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()
            self.drawing = True

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) and self.drawing:
            new_point = event.pos()
            self.lines.append((self.last_point, new_point))
            self.last_point = new_point
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def clear_canvas(self):
        self.lines = []
        self.update()

    def enable_drawing(self):
        self.drawing = True

    def save_image(self, file_path):
        image = self.grab()
        image.save(file_path)

    def load_image(self, file_path):
        pixmap = QPixmap(file_path)
        if not pixmap.isNull():
            self.clear_canvas()
            self.loaded_image = pixmap
            self.update()


    def enable_drawing(self):
        self.drawing = True

    def set_pen_color(self, color):
        self.pen_color = color
    
    def isModified(self):
        return bool(self.lines)
