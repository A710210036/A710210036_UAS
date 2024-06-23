import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Hello World')
        self.setGeometry(100, 100, 280, 80)
        self.label = QLabel('Hello, World!', self)
        self.label.move(100, 30)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())