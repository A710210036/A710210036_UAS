import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QComboBox

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Combobox Example')
        self.setGeometry(100, 100, 280, 80)
        
        self.label = QLabel('Select an option:', self)
        self.label.move(10, 20)
        
        self.combobox = QComboBox(self)
        self.combobox.addItem('Option 1')
        self.combobox.addItem('Option 2')
        self.combobox.addItem('Option 3')
        self.combobox.move(100, 20)
        self.combobox.currentIndexChanged.connect(self.on_combobox_change)
    
    def on_combobox_change(self, index):
        self.label.setText(f'Option {index + 1} Selected')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())