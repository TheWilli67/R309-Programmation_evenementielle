import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLineEdit


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.champ = QLineEdit()
        self.bouton = QPushButton("Valider")
        self.quitter = QPushButton("Quitter")
        self.quitter.clicked.connect(self.quitting)
        self.bouton.clicked.connect(self.appui_bouton_copie)
        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.bouton)
        layout.addWidget(self.label)
        layout.addWidget(self.quitter)
        self.setLayout(layout)
        self.setWindowTitle("Bonjour")
    def appui_bouton_copie(self):
        texte_a_copier = self.champ.text()
        self.label.setText("Bonjour " + texte_a_copier)
    def quitting(self):
        sys.exit()


app = QApplication.instance()
if not app:
    app = QApplication(sys.argv)
fen = Fenetre()
fen.show()

app.exec_()
