from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QHBoxLayout,
)

from PySide6.QtCore import QTimer

from models.global_state import vehicle

from communication.can_frame import CANFrame
from communication.message_ids import BODY_COMMAND
from communication.message_ids import (
    BODY_COMMAND,
    LOCK_DOORS,
    UNLOCK_DOORS,
    HEADLIGHT_ON,
    HEADLIGHT_OFF,
    LEFT_INDICATOR,
    RIGHT_INDICATOR,
    HAZARD,
)


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.bus = None

        self.setWindowTitle("AutoSimX Dashboard")
        self.resize(900,700)

        vehicle_box = QGroupBox("Vehicle Status")

        grid = QGridLayout()

        self.speed = QLabel()
        self.rpm = QLabel()
        self.fuel = QLabel()
        self.headlights = QLabel()
        self.doors = QLabel()

        grid.addWidget(QLabel("Speed"),0,0)
        grid.addWidget(self.speed,0,1)

        grid.addWidget(QLabel("RPM"),1,0)
        grid.addWidget(self.rpm,1,1)

        grid.addWidget(QLabel("Fuel"),2,0)
        grid.addWidget(self.fuel,2,1)

        grid.addWidget(QLabel("Headlights"),3,0)
        grid.addWidget(self.headlights,3,1)

        grid.addWidget(QLabel("Doors"),4,0)
        grid.addWidget(self.doors,4,1)

        vehicle_box.setLayout(grid)

        self.log = QTextEdit()
        self.log.setReadOnly(True)

        self.lock = QPushButton("Lock Doors")
        self.unlock = QPushButton("Unlock Doors")

        buttons = QHBoxLayout()

        buttons.addWidget(self.lock)
        buttons.addWidget(self.unlock)

        layout = QVBoxLayout()

        layout.addWidget(vehicle_box)
        layout.addWidget(self.log)
        layout.addLayout(buttons)

        self.setLayout(layout)

        self.lock.clicked.connect(
            lambda: self.send_command(LOCK_DOORS)
        )

        self.unlock.clicked.connect(
            lambda: self.send_command(UNLOCK_DOORS)
        )

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.refresh_dashboard
        )

        self.timer.start(100)

    def send_command(self, command):

        if self.bus is None:
            return

        frame = CANFrame(
            can_id=BODY_COMMAND,
            sender="Dashboard",
            data=[command]
        )

        self.bus.transmit(frame)

    def refresh_dashboard(self):

        self.speed.setText(f"{vehicle.speed} km/h")
        self.rpm.setText(str(vehicle.rpm))
        self.fuel.setText(f"{vehicle.fuel}%")

        self.headlights.setText(
            "ON" if vehicle.headlights else "OFF"
        )

        self.doors.setText(
            "LOCKED" if vehicle.door_locked else "UNLOCKED"
        )