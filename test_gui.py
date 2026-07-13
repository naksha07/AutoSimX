import sys

from PySide6.QtWidgets import QApplication

from gui.dashboard import Dashboard


app = QApplication(sys.argv)

window = Dashboard()

window.show()

app.exec()