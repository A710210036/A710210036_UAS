import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grid Layout Example')
        self.setGeometry(100, 100, 280, 100)
        
        layout = QGridLayout()
        
        layout.addWidget(QLabel('Name:'), 0, 0)
        layout.addWidget(QLineEdit(), 0, 1)
        
        layout.addWidget(QLabel('Email:'), 1, 0)
        layout.addWidget(QLineEdit(), 1, 1)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())