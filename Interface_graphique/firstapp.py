import sys
from PyQt5.QtWidgets import QApplication, QWidget
app = QApplication(sys.argv)
root = QWidget()
root.resize(600, 300)
root.setWindowTitle("Hello world!")
root.show()
if __name__ == '__main__':
    sys.exit(app.exec_())
