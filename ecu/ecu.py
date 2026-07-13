"""
Base ECU Module
"""

from communication.can_frame import CANFrame


class ECU:

    def __init__(self, name):

        self.name = name
        self.bus = None

    def send(self, frame: CANFrame):

        print(f"\n[{self.name}] Sending Frame...")

        if self.bus:
            self.bus.transmit(frame)
        else:
            print("No CAN Bus Connected!")

    def receive(self, frame: CANFrame):

        print(f"\n[{self.name}] Message Received!")

        frame.display()