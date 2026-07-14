from autosar.software_component import SoftwareComponent


class EngineComponent(SoftwareComponent):

    def __init__(self):

        super().__init__("Engine SWC")

    def update(self, speed, rpm):

        self.write("VehicleSpeed", speed)
        self.write("EngineRPM", rpm)