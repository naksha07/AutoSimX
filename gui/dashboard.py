"""
AutoSimX Dashboard
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QGroupBox,
    QGridLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
)

from PySide6.QtCore import QTimer

from models.global_state import vehicle
from models.can_history import history

from communication.can_frame import CANFrame
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
        self.resize(1000, 700)

        # ==========================================================
        # Vehicle Status
        # ==========================================================

        vehicle_box = QGroupBox("Vehicle Status")

        grid = QGridLayout()

        self.speed = QLabel()
        self.rpm = QLabel()
        self.fuel = QLabel()
        self.headlights = QLabel()
        self.doors = QLabel()

        grid.addWidget(QLabel("Speed"), 0, 0)
        grid.addWidget(self.speed, 0, 1)

        grid.addWidget(QLabel("RPM"), 1, 0)
        grid.addWidget(self.rpm, 1, 1)

        grid.addWidget(QLabel("Fuel"), 2, 0)
        grid.addWidget(self.fuel, 2, 1)

        grid.addWidget(QLabel("Headlights"), 3, 0)
        grid.addWidget(self.headlights, 3, 1)

        grid.addWidget(QLabel("Doors"), 4, 0)
        grid.addWidget(self.doors, 4, 1)

        vehicle_box.setLayout(grid)

        # ==========================================================
        # CAN Monitor
        # ==========================================================

        can_box = QGroupBox("Live CAN Monitor")

        can_layout = QVBoxLayout()

        self.can_table = QTableWidget()

        self.can_table.setColumnCount(5)

        self.can_table.setHorizontalHeaderLabels(
            [
                "Time",
                "CAN ID",
                "Sender",
                "DLC",
                "Data",
            ]
        )

        self.can_table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        self.can_table.verticalHeader().setVisible(False)

        self.can_table.setAlternatingRowColors(True)

        can_layout.addWidget(self.can_table)

        can_box.setLayout(can_layout)

        # ==========================================================
        # Log Window
        # ==========================================================

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        # ==========================================================
        # Buttons
        # ==========================================================

        self.lock = QPushButton("Lock Doors")

        self.unlock = QPushButton("Unlock Doors")

        buttons = QHBoxLayout()

        buttons.addWidget(self.lock)

        buttons.addWidget(self.unlock)

        # ==========================================================
        # Main Layout
        # ==========================================================

        layout = QVBoxLayout()

        layout.addWidget(vehicle_box)

        layout.addWidget(can_box)

        layout.addWidget(self.log)

        layout.addLayout(buttons)

        self.setLayout(layout)

        # ==========================================================
        # Button Connections
        # ==========================================================

        self.lock.clicked.connect(
            lambda: self.send_command(LOCK_DOORS)
        )

        self.unlock.clicked.connect(
            lambda: self.send_command(UNLOCK_DOORS)
        )

        # ==========================================================
        # Timer
        # ==========================================================

        self.timer = QTimer()

        self.timer.timeout.connect(self.refresh_dashboard)

        self.timer.start(100)

    # ==============================================================
    # Send CAN Command
    # ==============================================================

    def send_command(self, command):

        if self.bus is None:
            return

        frame = CANFrame(
            can_id=BODY_COMMAND,
            sender="Dashboard",
            data=[command],
        )

        self.bus.transmit(frame)

    # ==============================================================
    # Update CAN Monitor
    # ==============================================================

    def update_can_table(self):

        frames = history.get()

        self.can_table.setRowCount(len(frames))

        for row, frame in enumerate(frames):

            self.can_table.setItem(
                row,
                0,
                QTableWidgetItem(
                    frame.timestamp.strftime("%H:%M:%S")
                ),
            )

            self.can_table.setItem(
                row,
                1,
                QTableWidgetItem(hex(frame.can_id)),
            )

            self.can_table.setItem(
                row,
                2,
                QTableWidgetItem(frame.sender),
            )

            self.can_table.setItem(
                row,
                3,
                QTableWidgetItem(str(frame.dlc)),
            )

            self.can_table.setItem(
                row,
                4,
                QTableWidgetItem(
                    " ".join(
                        f"{byte:02X}" for byte in frame.data
                    )
                ),
            )

        self.can_table.scrollToBottom()

    # ==============================================================
    # Refresh Dashboard
    # ==============================================================

    def refresh_dashboard(self):

        self.speed.setText(f"{vehicle.speed} km/h")

        self.rpm.setText(str(vehicle.rpm))

        self.fuel.setText(f"{vehicle.fuel}%")

        self.headlights.setText(
            "ON" if vehicle.headlights else "OFF"
        )

        self.doors.setText(
            "LOCKED"
            if vehicle.door_locked
            else "UNLOCKED"
        )

        self.update_can_table()