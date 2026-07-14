"""
Virtual CAN Bus
"""

from communication.can_frame import CANFrame
from logger.can_logger import log_frame
from logger.csv_logger import csv_logger
from models.can_history import history


class CANBus:
    """
    Simulates a CAN Bus.
    """

    def __init__(self):
        self.ecus = {}

    def register_ecu(self, ecu):
        self.ecus[ecu.name] = ecu
        ecu.bus = self

        print(f"[BUS] {ecu.name} connected.")

    def transmit(self, frame: CANFrame):

        print("\n" + "=" * 60)
        print("[CAN BUS] Broadcasting Frame")
        print("=" * 60)

        frame.display()
        
        history.add(frame)

        csv_logger.log(frame)

        # Save the frame to logs/can.log
        log_frame(frame)

        from models.ecu_status import ecu_status
        
        ecu_status.heartbeat(frame.sender)

        # Broadcast to every ECU except sender
        for ecu in self.ecus.values():
            if ecu.name != frame.sender:
                ecu.receive(frame)