"""
Base ECU Module
"""

from communication.can_frame import CANFrame


class ECU:
    """
    Generic ECU.
    """

    def __init__(self, name: str):
        self.name = name

    def send(self, frame: CANFrame):
        """
        Send CAN Frame.
        """

        print(f"\n{self.name} transmitting...")
        frame.display()

    def receive(self, frame: CANFrame):
        """
        Receive CAN Frame.
        """

        print(f"\n{self.name} received a message.")
        frame.display()