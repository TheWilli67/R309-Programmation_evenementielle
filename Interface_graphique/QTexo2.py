import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, QGridLayout, QMessageBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.setWindowTitle("El convertisseur de Température")

        self.lbl = QLabel(self)
        self.lbl.setText("Température :")

        self.champ = QLineEdit(self)

        self.lbl2 = QLabel(self)
        self.lbl2.setText("°C")

        self.bouton = QPushButton(self)
        self.bouton.setText("Convertir")
        self.bouton.clicked.connect(self.calcul)

        self.combobox = QComboBox()
        self.combobox.addItem("°C -> K")
        self.combobox.addItem("K -> °C")
        self.combobox.currentIndexChanged.connect(self.action)

        self.lbl3 = QLabel(self)
        self.lbl3.setText("Conversion : ")

        self.lbl4 = QLabel(self)
        self.lbl4.setText("")

        self.lbl5 = QLabel(self)
        self.lbl5.setText("K")

        self.bouton2 = QPushButton(self)
        self.bouton2.setText("?")
        self.bouton2.clicked.connect(self.help)

        grid.addWidget(self.lbl, 1, 1)
        grid.addWidget(self.champ, 1, 2)
        grid.addWidget(self.lbl2, 1, 3)
        grid.addWidget(self.bouton, 2, 2)
        grid.addWidget(self.combobox, 2, 3)
        grid.addWidget(self.lbl3, 3, 1)
        grid.addWidget(self.lbl4, 3, 2)
        grid.addWidget(self.lbl5, 3, 3)
        grid.addWidget(self.bouton2, 3, 4)

    def action(self):
        if self.combobox.currentIndex() == 0:
            self.lbl5.setText("K")
            self.lbl2.setText("°C")
        if self.combobox.currentIndex() == 1:
            self.lbl5.setText("°C")
            self.lbl2.setText("K")

    def calcul(self):
        try:
            float(self.champ.text())
        except:
            self.box = QMessageBox(self)
            self.box.setWindowTitle("Aide")
            self.box.setText("Ce n'est pas un float")
            self.box.show()
            return 0
        if self.combobox.currentIndex() == 0:
            if -273.15 > float(self.champ.text()):
                self.box2 = QMessageBox(self)
                self.box2.setWindowTitle("Aide")
                self.box2.setText("valeur en dessou du 0 absolu")
                self.box2.show()
            else:
                conversion = float(self.champ.text()) + 273.15
                self.lbl4.setText(str(conversion))

        if self.combobox.currentIndex() == 1:
            if 0 > float(self.champ.text()):
                self.box3 = QMessageBox(self)
                self.box3.setWindowTitle("Aide")
                self.box3.setText("valeur en dessou du 0 absolu")
                self.box3.show()
            else:
                conversion = float(self.champ.text()) - 273.15
                self.lbl4.setText(str(conversion))

    def help(self):
        self.box = QMessageBox(self)
        self.box.setWindowTitle("Aide")
        self.box.setText(
            "Permet de convertir un nombre soit de Kelvin vers Celcius vers kelvin")
        self.box.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
