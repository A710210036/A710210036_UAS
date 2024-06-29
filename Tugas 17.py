import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QProgressBar, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Slider and Progress Bar')
        self.setGeometry(100, 100, 280, 120)
        
        layout = QVBoxLayout()
        
        self.slider = QSlider()
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.on_slider_change)
        
        self.progress_bar = QProgressBar()
        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        
        layout.addWidget(self.slider)
        layout.addWidget(self.progress_bar)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
    
    def on_slider_change(self, value):
        self.progress_bar.setValue(value)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())