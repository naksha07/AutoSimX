"""
Base ECU Module
"""

import time

from communication.can_frame import CANFrame
from communication.message_ids import HEARTBEAT


class ECU:

    def __init__(self, name):

        # THIS LINE WAS MISSING
        self.name = name

        self.bus = None

        self.frames_sent = 0
        self.frames_received = 0

    def send(self, frame: CANFrame):

        self.frames_sent += 1

        if self.bus:
            print(f"\n[{self.name}] Sending Frame...")
            self.bus.transmit(frame)

    def receive(self, frame: CANFrame):

        self.frames_received += 1

        print(f"{self.name} received frame {hex(frame.can_id)}")

    def heartbeat(self):

        while True:

            frame = CANFrame(
                can_id=HEARTBEAT,
                sender=self.name,
                data=[1]
            )

            self.send(frame)

            time.sleep(5)

    def statistics(self):

        print("\n----------------------------")
        print(self.name)
        print("----------------------------")
        print(f"Frames Sent     : {self.frames_sent}")
        print(f"Frames Received : {self.frames_received}")