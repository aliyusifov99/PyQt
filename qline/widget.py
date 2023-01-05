from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QMessageBox, QLabel, QLineEdit,QHBoxLayout\
    

class Widget(QWidget):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle('Qlabel and Qlineedit')
        
        label = QLabel('Full name:')
        self.line_edit = QLineEdit()
        button = QPushButton('Grab Data')
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel('I AM HERE')
        
        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)
        
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)
        
        self.setLayout(v_layout)
        
    def button_clicked(self):
        print('Full name: ', self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())
        
    