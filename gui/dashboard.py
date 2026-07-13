from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class Dashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("AutoSimX Dashboard")

        self.setMinimumSize(700, 600)

        self.speed = QLabel("Speed : 0 km/h")

        self.rpm = QLabel("RPM : 800")

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.lock_button = QPushButton("Lock Doors")

        self.unlock_button = QPushButton("Unlock Doors")

        layout = QVBoxLayout()

        layout.addWidget(self.speed)

        layout.addWidget(self.rpm)

        layout.addWidget(self.log)

        layout.addWidget(self.lock_button)

        layout.addWidget(self.unlock_button)

        self.setLayout(layout)