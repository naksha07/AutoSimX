"""
AutoSimX Launcher
Runs ECU Simulation + GUI together.
"""

import sys
import threading

from PySide6.QtWidgets import QApplication

from gui.dashboard import Dashboard

from communication.can_bus import CANBus

from ecu.engine_ecu import EngineECU
from ecu.cluster_ecu import ClusterECU
from ecu.body_ecu import BodyECU
from ecu.gateway_ecu import GatewayECU


def start_backend():

    bus = CANBus()

    engine = EngineECU()
    cluster = ClusterECU()
    body = BodyECU()
    gateway = GatewayECU()

    bus.register_ecu(engine)
    bus.register_ecu(cluster)
    bus.register_ecu(body)
    bus.register_ecu(gateway)

    # Only drive simulation for now
    engine.simulate_drive()


if __name__ == "__main__":

    backend = threading.Thread(
        target=start_backend,
        daemon=True
    )

    backend.start()

    app = QApplication(sys.argv)

    dashboard = Dashboard()

    dashboard.show()

    sys.exit(app.exec())