import sys
from PyQt5.QtWidgets import * 
app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)

        grid = QGridLayout()
        widget.setLayout(grid)

        ok = QPushButton("Ok")
        quit = QPushButton("Quitter")
        ok.clicked.connect(self.actionOk)
        quit.clicked.connect(self.actionQuitter)

    def _actionOk(self):
        pass


    def _actionQuitter(self):
        QCoreApplication.exit(0)


if __name__ == '__main__':
    sys.exit(app.exec_())
