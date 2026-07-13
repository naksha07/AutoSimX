"""
Virtual CAN Bus
"""

from communication.can_frame import CANFrame
from logger.can_logger import log_frame


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

        # Save the frame to logs/can.log
        log_frame(frame)

        # Broadcast to every ECU except sender
        for ecu in self.ecus.values():
            if ecu.name != frame.sender:
                ecu.receive(frame)