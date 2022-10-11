#-*- UTF-8 -*-

import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QFont
from PyQt5. QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.pix1 = None
        self.pix2 = None

        self. initUI()

    def initUI(self):
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle("Draw text")
        self.pix1 = QPixmap(self.size())
        self.pix2 = QPixmap(self.size())
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pix1)
        painter.drawPixmap(0, 0, self.pix2)

    def draw(self):
        _color = QColor(Qt.white)
        #_color.setAlphaF(0.4)
        self.pix1.fill(_color)
        painter = QPainter(self.pix1)
        painter.setPen(Qt.red)
        painter.drawText(100, 100, "图层1，我们绘制了一些文字")

        _color = QColor(Qt.white)
        _color.setAlphaF(0)
        self.pix2.fill(_color)
        painter = QPainter(self.pix2)
        painter.setPen(Qt.blue)
        painter.drawText(200, 200, "最上层，我们又绘制了一些文字")


if __name__ == "__main__":
    app = QApplication (sys. argv)
    ex = Example()
    ex.draw()
    sys.exit (app.exec())
