import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Управление НЛО")
        self.label = QLabel(self)
        pxmp = QPixmap("ufo.png")
        self.cordX = 134
        self.cordY = 134
        self.label.setGeometry(self.cordX, self.cordY, 32, 32)
        self.label.setPixmap(pxmp)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.cordY -= 10
            if self.cordY < 0:
                self.cordY = 268
        elif event.key() == Qt.Key_Down:
            self.cordY += 10
            self.cordY %= 268
        elif event.key() == Qt.Key_Left:
            self.cordX -= 10
            if self.cordX < 0:
                self.cordX = 268
        elif event.key() == Qt.Key_Right:
            self.cordX += 10
            self.cordX %= 268
        self.label.move(self.cordX, self.cordY)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    sys.exit(app.exec_())
