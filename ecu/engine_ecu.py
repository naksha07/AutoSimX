from ecu.ecu import ECU
from communication.can_frame import CANFrame


class EngineECU(ECU):

    def __init__(self):

        super().__init__("Engine ECU")

        self.speed = 0
        self.rpm = 0

    def update_engine(self, speed, rpm):

        self.speed = speed
        self.rpm = rpm

        frame = CANFrame(
            can_id=0x101,
            sender=self.name,
            receiver="Cluster ECU",
            data=[speed, rpm // 100]
        )

        self.send(frame)