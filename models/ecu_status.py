"""
ECU Health Monitor
"""

from datetime import datetime


class ECUStatus:

    def __init__(self):

        self.status = {
            "Engine ECU": datetime.now(),
            "Cluster ECU": datetime.now(),
            "Body ECU": datetime.now(),
            "Gateway ECU": datetime.now(),
        }

    def heartbeat(self, ecu):

        self.status[ecu] = datetime.now()

    def is_alive(self, ecu):

        delta = datetime.now() - self.status[ecu]

        return delta.total_seconds() < 2

    def get_status(self):

        return self.status


ecu_status = ECUStatus()