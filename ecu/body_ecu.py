from ecu.ecu import ECU


class BodyECU(ECU):

    def __init__(self):

        super().__init__("Body ECU")

        self.headlights = False
        self.door_locked = True