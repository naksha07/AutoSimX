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

    def transmit(self, frame: CANFrame):

        print("\n" + "=" * 60)
        print("[CAN BUS] Transmitting Frame")
        print("=" * 60)

        frame.display()

        receiver = self.ecus.get(frame.receiver)

        if receiver:
            receiver.receive(frame)
        else:
            print(f"[BUS] Receiver '{frame.receiver}' not found.")