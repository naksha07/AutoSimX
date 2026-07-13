from ecu.ecu import ECU


class ClusterECU(ECU):

    def __init__(self):

        super().__init__("Cluster ECU")

    def receive(self, frame):
        if frame.can_id != 0x101:
            return
        speed = frame.data[0]
        rpm = frame.data[1] * 100
        
        print("\n==============================")
        print(" INSTRUMENT CLUSTER ")
        print("==============================")
        print(f" Speed : {speed:3} km/h")
        print(f" RPM   : {rpm}")
        print("==============================")