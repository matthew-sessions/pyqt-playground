import sys
from main import MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication()
    w = MainWindow()
    w.show()
    sys.exit(app.exec())