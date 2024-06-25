import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Line Edit')
        self.setGeometry(100, 100, 280, 80)
        
        self.label = QLabel('Enter text:', self)
        self.label.move(10, 20)
        
        self.line_edit = QLineEdit(self)
        self.line_edit.move(100, 20)
        self.line_edit.textChanged.connect(self.on_text_change)
    
    def on_text_change(self, text):
        self.label.setText(text)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())