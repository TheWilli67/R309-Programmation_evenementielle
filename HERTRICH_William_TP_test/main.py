########################################################################
# lien Github :
# https://github.com/TheWilli67/R309-Programmation_evenementielle/tree/main/HERTRICH_William_TP_test
########################################################################


import sys
import time
import multiprocessing
import socket
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QVBoxLayout, QLabel, QLCDNumber, QLineEdit


class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.champ = QLabel()
        self.start = QPushButton("Start")
        self.reset = QPushButton("Reset")
        self.stop = QPushButton("Stop")
        self.connect = QPushButton("Connect")
        self.quitter = QPushButton("Quitter")
        self.quitter.clicked.connect(self.quitting)
        self.start.clicked.connect(self.appui_start)
        self.connect.clicked.connect(self.connection)
        self.label = QLabel()
        
        layout = QVBoxLayout()
        layout.addWidget(self.champ)
        layout.addWidget(self.start)
        layout.addWidget(self.reset)
        layout.addWidget(self.stop)
        layout.addWidget(self.connect)
        layout.addWidget(self.label)
        layout.addWidget(self.quitter)
        self.setLayout(layout)
        self.setWindowTitle("Chronomètre")

    def appui_start(self):
        while True:
            start = time.perf_counter()
            p1 = multiprocessing.Process()
            p1.start()
            self.champ.setText(start)
            
    def connection(self):
        socket.connect(('127.0.0.1', 10000))

    def quitting(self):
        sys.exit()
    
    


app = QApplication.instance()

if not app:
    app = QApplication(sys.argv)
fen = Fenetre()
fen.show()

app.exec_()
