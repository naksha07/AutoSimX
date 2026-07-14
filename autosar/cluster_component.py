from autosar.software_component import SoftwareComponent


class ClusterComponent(SoftwareComponent):

    def __init__(self):

        super().__init__("Cluster SWC")

    def display(self):

        speed = self.read("VehicleSpeed")
        rpm = self.read("EngineRPM")

        print("\n[AUTOSAR Cluster SWC]")
        print("Vehicle Speed :", speed)
        print("Engine RPM    :", rpm)