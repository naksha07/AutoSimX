"""
Virtual CAN Bus
"""

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

        print(">>> NEW CAN BUS IS RUNNING <<<")

        print("\n" + "=" * 60)
        print("[CAN BUS] Broadcasting Frame")
        print("=" * 60)

        frame.display()

        from logger.can_logger import log
        log(frame)

        for ecu in self.ecus.values():
            if ecu.name != frame.sender:
                ecu.receive(frame)