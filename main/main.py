"""
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

window  = QMainWindow()
window.setWindowTitle('My first Windows app')

button  = QPushButton()
button.setText('Press me')

window.setCentralWidget(button)

window.show()
app.exec()
"""

"""
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


        
app = QApplication(sys.argv)

window  = ButtonHolder()

window.show()
app.exec()
"""
"""
import sys
from PySide6.QtWidgets import QApplication
from button_holder import ButtonHolder

def button_clicked():
    print('You clicked the button?')
        
app = QApplication(sys.argv)

button  = ButtonHolder()
button.show()
app.exec()
"""

"""
import sys
from PySide6.QtWidgets import QApplication, QPushButton, QSlider
from button_holder import ButtonHolder

# def button_clicked():
#     print('You clicked the button?')

def respond_to_slider(data):
    print(f'Slider moved to: {data}')
app = QApplication(sys.argv)

# button  = QPushButton()
# button.setCheckable(True)
# button.clicked.connect(button_clicked)
slider = QSlider()
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()
"""
"""from PySide6.QtWidgets import QApplication, QWidget
from rockwidget import RockWidget
import sys
app  = QApplication(sys.argv)

window = RockWidget()
window.show()
app.exec()
"""

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow

import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()
print('hello')
app.exec()