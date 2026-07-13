from ecu.ecu import ECU


class GatewayECU(ECU):

    def __init__(self):

        super().__init__("Gateway ECU")

    def receive(self, frame):

        print(
            f"[Gateway] {frame.sender} -> "
            f"{hex(frame.can_id)} | DATA = {frame.data}"
        )