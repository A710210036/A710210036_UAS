import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Message Box')
        self.setGeometry(100, 100, 280, 80)
        
        self.button = QPushButton('Show Message', self)
        self.button.move(100, 30)
        self.button.clicked.connect(self.show_message)
    
    def show_message(self):
        QMessageBox.information(self, 'Message', 'Hello, this is a message box.')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())