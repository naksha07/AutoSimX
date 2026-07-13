from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QGroupBox,
    QGridLayout
)

from PySide6.QtCore import QTimer

from models.global_state import vehicle


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("AutoSimX Automotive Dashboard")

        self.resize(900, 700)

        vehicle_box = QGroupBox("Vehicle Information")

        grid = QGridLayout()

        self.speed = QLabel()

        self.rpm = QLabel()

        self.fuel = QLabel()

        self.headlights = QLabel()

        self.door = QLabel()

        grid.addWidget(QLabel("Speed"), 0, 0)
        grid.addWidget(self.speed, 0, 1)

        grid.addWidget(QLabel("RPM"), 1, 0)
        grid.addWidget(self.rpm, 1, 1)

        grid.addWidget(QLabel("Fuel"), 2, 0)
        grid.addWidget(self.fuel, 2, 1)

        grid.addWidget(QLabel("Headlights"), 3, 0)
        grid.addWidget(self.headlights, 3, 1)

        grid.addWidget(QLabel("Doors"), 4, 0)
        grid.addWidget(self.door, 4, 1)

        vehicle_box.setLayout(grid)

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        self.lock = QPushButton("Lock Doors")

        self.unlock = QPushButton("Unlock Doors")

        layout = QVBoxLayout()

        layout.addWidget(vehicle_box)

        layout.addWidget(self.log)

        layout.addWidget(self.lock)

        layout.addWidget(self.unlock)

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(self.refresh_dashboard)

        self.timer.start(100)

    def refresh_dashboard(self):

        self.speed.setText(f"{vehicle.speed} km/h")

        self.rpm.setText(str(vehicle.rpm))

        self.fuel.setText(f"{vehicle.fuel} %")

        self.headlights.setText(
            "ON" if vehicle.headlights else "OFF"
        )

        self.door.setText(
            "LOCKED" if vehicle.door_locked else "UNLOCKED"
        )