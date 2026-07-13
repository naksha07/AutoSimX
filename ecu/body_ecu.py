from ecu.ecu import ECU

from communication.message_ids import ENGINE_STATUS

from models.global_state import vehicle


class BodyECU(ECU):

    def __init__(self):

        super().__init__("Body ECU")

    def receive(self, frame):

        self.frames_received += 1

        if frame.can_id != ENGINE_STATUS:
            return

        speed = frame.data[0]

        vehicle.headlights = speed > 60

        print(
            f"[Body ECU] Headlights : "
            f"{'ON' if vehicle.headlights else 'OFF'}"
        )