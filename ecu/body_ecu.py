from ecu.ecu import ECU


class BodyECU(ECU):

    def __init__(self):

        super().__init__("Body ECU")

        self.headlights = False
        self.door_locked = True

    def receive(self, frame):
        
        if frame.can_id == 0x101:
            speed = frame.data[0]
        
            self.headlights = speed > 60
                
                
            print(
                f"[Body ECU] Headlights: "
                f"{'ON' if self.headlights else 'OFF'}"
            )