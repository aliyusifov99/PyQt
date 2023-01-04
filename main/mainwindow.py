from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app=app
        self.setWindowTitle('Custom MainWindow')
        
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('&File')  
        quit_action = file_menu.addAction('Quit')
        quit_action.triggered.connect(self.quit_app)
        
        edit_menu = menu_bar.addMenu('Edit')
        edit_menu.addAction('Copy')
        edit_menu.addAction('Cut')
        edit_menu.addAction('Paste')
        edit_menu.addAction('Undo')
        edit_menu.addAction('Redo')
        
        menu_bar.addMenu('Window')
        menu_bar.addMenu('Setting')
        menu_bar.addMenu('Help')
        
        toolbar =  QToolBar('My main toolbar')
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)
        
        action1 = QAction('Some actoion', self)
        action1.setStatusTip('Status message for some action')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)
        
        toolbar.addSeparator()
        toolbar.addWidget(QPushButton('Click here'))

        self.setStatusBar(QStatusBar(self))
        
        
    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        self.statusBar().showMessage('Message from my app')