from ecu.ecu import ECU
from communication.can_frame import CANFrame
import time
from communication.message_ids import ENGINE_STATUS


class EngineECU(ECU):

    def __init__(self):
        super().__init__("Engine ECU")

        self.speed = 0
        self.rpm = 800

    def simulate_drive(self):

        # Accelerate
        for speed in range(0, 101, 20):

            rpm = 800 + speed * 25

            frame = CANFrame(
                can_id= ENGINE_STATUS,
                sender=self.name,
                data=[speed, rpm // 100]
            )

            self.send(frame)

            time.sleep(1)

            print("\n========== Simulation Complete ==========")

        # Decelerate
        for speed in range(80, -1, -20):

            rpm = 800 + speed * 25

            frame = CANFrame(
                can_id=0x101,
                sender=self.name,
                data=[speed, rpm // 100]
            )

            self.send(frame)

            time.sleep(1)