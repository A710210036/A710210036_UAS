import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Checkbox Example')
        self.setGeometry(100, 100, 280, 80)
        
        self.label = QLabel('Select an option:', self)
        self.label.move(10, 20)
        
        self.checkbox = QCheckBox('Option 1', self)
        self.checkbox.move(100, 20)
        self.checkbox.stateChanged.connect(self.on_state_change)
    
    def on_state_change(self, state):
        if state == 2:
            self.label.setText('Option 1 Selected')
        else:
            self.label.setText('Option 1 Deselected')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())