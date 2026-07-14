import csv
import time

from communication.can_frame import CANFrame


class CANReplay:

    def __init__(self, bus):

        self.bus = bus

    def replay(self, filename="logs/can_log.csv"):

        print("\n==============================")
        print("   CAN Replay Started")
        print("==============================\n")

        with open(filename, newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                can_id = int(row["CAN_ID"], 16)

                sender = row["Sender"]

                data = [
                    int(byte, 16)
                    for byte in row["Data"].split()
                ]

                frame = CANFrame(
                    can_id=can_id,
                    sender=sender,
                    data=data,
                )

                self.bus.transmit(frame)

                time.sleep(1)

        print("\n==============================")
        print(" Replay Finished")
        print("==============================")