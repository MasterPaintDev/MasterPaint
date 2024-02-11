from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QPoint

class DrawingWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.last_point = QPoint()
        self.drawing = False
        self.lines = []

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
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

    def clear_drawing(self):
        self.lines = []
        self.update()
