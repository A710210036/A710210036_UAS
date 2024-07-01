import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Dialog')
        self.setGeometry(100, 100, 400, 80)
        
        self.label = QLabel('Selected file:', self)
        self.label.move(20, 20)
        
        self.button = QPushButton('Open File', self)
        self.button.move(20, 50)
        self.button.clicked.connect(self.open_file)
    
    def open_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*);;Python Files (*.py)', options=options)
        if file_name:
            self.label.setText(f'Selected file: {file_name}')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())