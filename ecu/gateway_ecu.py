from ecu.ecu import ECU


class GatewayECU(ECU):

    def __init__(self):

        super().__init__("Gateway ECU")

    def receive(self, frame):

        print(
            f"[Gateway] Logged Frame -> "
            f"{hex(frame.can_id)} from {frame.sender}"
        )