from ecu.ecu import ECU


class ClusterECU(ECU):

    def __init__(self):

        super().__init__("Cluster ECU")

    def receive(self, frame):

        print("\n===== Instrument Cluster =====")

        speed = frame.data[0]

        rpm = frame.data[1] * 100

        print(f"Vehicle Speed : {speed} km/h")

        print(f"Engine RPM    : {rpm}")

        print("==============================")