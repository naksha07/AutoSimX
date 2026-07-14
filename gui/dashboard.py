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
    QProgressBar,
)

from PySide6.QtCore import QTimer
from datetime import datetime

from models.global_state import vehicle
from models.ecu_status import ecu_status
from models.can_history import history
from models.dtc_manager import dtc_manager

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

from diagnostics.dtc_codes import (
    ENGINE_OVERHEAT,
    LOW_FUEL,
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

        self.speed = QLabel("0 km/h")
        self.rpm = QLabel("800")
        self.fuel = QLabel("100 %")

        font = self.speed.font()
        font.setPointSize(22)
        font.setBold(True)

        self.speed.setFont(font)
        self.rpm.setFont(font)
        self.fuel.setFont(font)

        self.headlights = QLabel()
        self.doors = QLabel()

        self.speed_bar = QProgressBar()
        self.speed_bar.setMaximum(240)

        self.rpm_bar = QProgressBar()
        self.rpm_bar.setMaximum(8000)

        self.fuel_bar = QProgressBar()
        self.fuel_bar.setMaximum(100)

        grid.addWidget(QLabel("Speed"), 0, 0)
        grid.addWidget(self.speed, 0, 1)
        grid.addWidget(self.speed_bar, 0, 2)

        grid.addWidget(QLabel("RPM"), 1, 0)
        grid.addWidget(self.rpm, 1, 1)
        grid.addWidget(self.rpm_bar, 1, 2)

        grid.addWidget(QLabel("Fuel"), 2, 0)
        grid.addWidget(self.fuel, 2, 1)
        grid.addWidget(self.fuel_bar, 2, 2)

        grid.addWidget(QLabel("Headlights"), 3, 0)
        grid.addWidget(self.headlights, 3, 1)

        grid.addWidget(QLabel("Doors"), 4, 0)
        grid.addWidget(self.doors, 4, 1)

        vehicle_box.setLayout(grid)

        # ==========================================================
        # ECU Health
        # ==========================================================

        ecu_box = QGroupBox("ECU Health")

        ecu_layout = QGridLayout()

        self.engine_led = QLabel()
        self.cluster_led = QLabel()
        self.body_led = QLabel()
        self.gateway_led = QLabel()

        ecu_layout.addWidget(QLabel("Engine ECU"), 0, 0)
        ecu_layout.addWidget(self.engine_led, 0, 1)

        ecu_layout.addWidget(QLabel("Cluster ECU"), 1, 0)
        ecu_layout.addWidget(self.cluster_led, 1, 1)

        ecu_layout.addWidget(QLabel("Body ECU"), 2, 0)
        ecu_layout.addWidget(self.body_led, 2, 1)

        ecu_layout.addWidget(QLabel("Gateway ECU"), 3, 0)
        ecu_layout.addWidget(self.gateway_led, 3, 1)

        ecu_box.setLayout(ecu_layout)

        # ==========================================================
        # Diagnostic Trouble Codes
        # ==========================================================

        dtc_box = QGroupBox("Diagnostic Trouble Codes")

        dtc_layout = QVBoxLayout()

        self.dtc_log = QTextEdit()

        self.dtc_log.setReadOnly(True)

        dtc_layout.addWidget(self.dtc_log)

        self.check_engine = QLabel("🟢 No Fault")

        clear_button = QPushButton("Clear DTC")

        inject_overheat = QPushButton("Inject Overheat")

        inject_lowfuel = QPushButton("Inject Low Fuel")

        dtc_layout.addWidget(self.check_engine)

        dtc_layout.addWidget(clear_button)

        dtc_layout.addWidget(inject_overheat)

        dtc_layout.addWidget(inject_lowfuel)

        dtc_box.setLayout(dtc_layout)

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
        layout.addWidget(ecu_box)
        layout.addWidget(dtc_box)
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

        clear_button.clicked.connect(self.clear_dtcs)

        inject_overheat.clicked.connect(
            lambda: dtc_manager.add(ENGINE_OVERHEAT)
        )

        inject_lowfuel.clicked.connect(
            lambda: dtc_manager.add(LOW_FUEL)
        )

        # ==========================================================
        # Timer
        # ==========================================================

        self.timer = QTimer()

        self.timer.timeout.connect(self.refresh_dashboard)

        self.timer.start(100)

        # ==========================================================
        # Stylesheet - Make headings larger and clearly visible
        # ==========================================================

        self.setStyleSheet("""
QWidget{
    background:#202124;
    color:white;
    font-size:12pt;
}

QGroupBox{
    border:2px solid #4CAF50;
    margin-top:10px;
    font-weight:bold;
}

QGroupBox::title {
    font-size: 16pt;
    font-weight: bold;
    color: #4CAF50;
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px 0 5px;
}

QProgressBar{
    border:1px solid gray;
    text-align:center;
    height:20px;
}

QProgressBar::chunk{
    background:#00C853;
}

QPushButton{
    background:#1976D2;
    color:white;
    padding:8px;
}

QPushButton:hover{
    background:#1565C0;
}
""")

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
    # ECU Health
    # ==============================================================

    def update_ecu_health(self):

        now = datetime.now()

        for ecu, last in ecu_status.get_status().items():

            delta = (now - last).total_seconds()

            state = "🟢 ONLINE" if delta < 2 else "🔴 OFFLINE"

            if ecu == "Engine ECU":
                self.engine_led.setText(state)

            elif ecu == "Cluster ECU":
                self.cluster_led.setText(state)

            elif ecu == "Body ECU":
                self.body_led.setText(state)

            elif ecu == "Gateway ECU":
                self.gateway_led.setText(state)

    # ==============================================================
    # DTC Update
    # ==============================================================

    def update_dtc(self):

        self.dtc_log.clear()

        dtcs = dtc_manager.get()

        if not dtcs:

            self.check_engine.setText("🟢 No Fault")

            self.dtc_log.append("No Active DTC")

            return

        self.check_engine.setText("🔴 CHECK ENGINE")

        for dtc in dtcs:

            self.dtc_log.append(

                f"[{dtc['time'].strftime('%H:%M:%S')}] "
                f"{dtc['code']} - {dtc['description']}" 
            )

    # ==============================================================
    # Clear DTCs
    # ==============================================================

    def clear_dtcs(self):

        dtc_manager.clear()

    # ==============================================================
    # CAN Monitor
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
        self.speed_bar.setValue(vehicle.speed)

        self.rpm.setText(str(vehicle.rpm))
        self.rpm_bar.setValue(vehicle.rpm)

        self.fuel.setText(f"{vehicle.fuel}%")
        self.fuel_bar.setValue(vehicle.fuel)

        self.headlights.setText(
            "ON" if vehicle.headlights else "OFF"
        )

        self.doors.setText(
            "LOCKED"
            if vehicle.door_locked
            else "UNLOCKED"
        )

        self.update_ecu_health()
        self.update_dtc()
        self.update_can_table()