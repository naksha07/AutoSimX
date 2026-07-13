from ecu.ecu import ECU
from communication.message_ids import HEARTBEAT


class GatewayECU(ECU):

    def __init__(self):
        super().__init__("Gateway ECU")

    def receive(self, frame):

        self.frames_received += 1

        if frame.can_id == HEARTBEAT:

            print(f"[Gateway] {frame.sender} is ONLINE")

        else:

            print(
                f"[Gateway] {frame.sender} -> "
                f"{hex(frame.can_id)} | DATA = {frame.data}"
            )