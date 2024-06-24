import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Button Click')
        self.setGeometry(100, 100, 280, 80)
        
        self.label = QLabel('Click the button', self)
        self.label.move(100, 30)
        
        self.button = QPushButton('Click Me', self)
        self.button.move(100, 50)
        self.button.clicked.connect(self.on_click)
    
    def on_click(self):
        self.label.setText('Button Clicked!')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())