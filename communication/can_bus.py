"""
Virtual CAN Bus
"""
from logger.can_logger import log_frame
from communication.can_frame import CANFrame


class CANBus:
    """
    Simulates a CAN Bus.
    """

    def __init__(self):
        self.ecus = {}

    def register_ecu(self, ecu):
        """
        Register an ECU on the CAN bus.
        """
        self.ecus[ecu.name] = ecu
        ecu.bus = self

        print(f"[BUS] {ecu.name} connected.")

    def transmit(self, frame):

        print("\n" + "=" * 60)
        print("[CAN BUS] Broadcasting Frame")
        print("=" * 60)

        frame.display()

        log_frame(frame)

        from logger.can_logger import log
        log(frame)

        for ecu in self.ecus.values():
            if ecu.name != frame.sender:
                ecu.receive(frame)