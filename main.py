import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.run)
        self.flag = False

    def run(self):
        self.flag = True
        self.repaint()

    def paintEvent(self, e):
        if self.flag:
            self.flag = False
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor('yellow'))
            self.draw_circle(qp)
            qp.end()

    def draw_circle(self, qp):
        x = randrange(0, 500)
        y = randrange(0, 400)
        r = randrange(50, 200)
        qp.drawEllipse(int(x), int(y), int(r), int(r))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
