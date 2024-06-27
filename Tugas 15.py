import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QRadioButton, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Radio Button Example')
        self.setGeometry(100, 100, 280, 120)
        
        self.label = QLabel('Select an option:', self)
        self.label.move(10, 20)
        
        self.radio1 = QRadioButton('Option 1', self)
        self.radio1.move(100, 20)
        self.radio1.toggled.connect(self.on_radio_toggle)
        
        self.radio2 = QRadioButton('Option 2', self)
        self.radio2.move(100, 40)
        self.radio2.toggled.connect(self.on_radio_toggle)
    
    def on_radio_toggle(self):
        if self.radio1.isChecked():
            self.label.setText('Option 1 Selected')
        elif self.radio2.isChecked():
            self.label.setText('Option 2 Selected')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())