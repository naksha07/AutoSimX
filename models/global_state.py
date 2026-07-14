"""
Global Vehicle State
"""


class VehicleState:

    def __init__(self):

        self.speed = 0
        self.rpm = 800
        self.fuel = 100

        self.headlights = False
        self.door_locked = False

        self.engine_temperature = 90


vehicle = VehicleState()