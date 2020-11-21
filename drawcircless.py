from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
import sys
from random import randint
from PyQt5 import uic


class Drawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.ccc.clicked.connect(self.drawer)
        canvas = QPixmap(600, 600)
        self.todraw.setPixmap(canvas)

    def drawer(self):
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]
        painter = QPainter(self.todraw.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0)) # *[randint(0, 255) for i in range(3)])
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Drawer()
    w.show()
    sys.exit(app.exec_())
