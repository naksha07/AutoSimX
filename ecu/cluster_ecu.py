from ecu.ecu import ECU
from communication.message_ids import ENGINE_STATUS


class ClusterECU(ECU):

    def __init__(self):
        super().__init__("Cluster ECU")

    def receive(self, frame):

        self.frames_received += 1

        if frame.can_id != ENGINE_STATUS:
            return

        speed = frame.data[0]
        rpm = frame.data[1] * 100

        print("\n==============================")
        print("      INSTRUMENT CLUSTER")
        print("==============================")
        print(f"Speed : {speed:3} km/h")
        print(f"RPM   : {rpm}")
        print("==============================")