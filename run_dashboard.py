"""
AutoSimX Launcher
"""

import sys
import threading

from PySide6.QtWidgets import QApplication

from communication.can_bus import CANBus

from ecu.engine_ecu import EngineECU
from ecu.cluster_ecu import ClusterECU
from ecu.body_ecu import BodyECU
from ecu.gateway_ecu import GatewayECU

from gui.dashboard import Dashboard


bus = CANBus()


def backend():

    engine = EngineECU()
    cluster = ClusterECU()
    body = BodyECU()
    gateway = GatewayECU()

    bus.register_ecu(engine)
    bus.register_ecu(cluster)
    bus.register_ecu(body)
    bus.register_ecu(gateway)

    engine.simulate_drive()


if __name__ == "__main__":

    threading.Thread(
        target=backend,
        daemon=True
    ).start()

    app = QApplication(sys.argv)

    dashboard = Dashboard()

    dashboard.bus = bus

    dashboard.show()

    sys.exit(app.exec())