from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFrame, QHBoxLayout, QSplitter, QLineEdit
import sys 
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtGui


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Учебный стенд")
        self.setFixedSize(QSize(500, 300))


        # Устанавливаем центральный виджет Window.

        hbox=QHBoxLayout()
        left=QFrame() 
       

        splitter1=QSplitter(Qt.Horizontal)
        lineedit=QLineEdit()
        
        splitter1.addWidget(left)
        splitter1.addWidget(lineedit)
        splitter1.setSizes([100,100])


# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
app = QApplication(sys.argv)

# Создаём виджет Qt — окно.
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()