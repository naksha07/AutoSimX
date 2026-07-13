"""
Vehicle State
Stores all vehicle information.
"""


class VehicleState:

    def __init__(self):

        self.speed = 0
        self.rpm = 800

        self.headlights = False

        self.door_locked = True

        self.left_indicator = False

        self.right_indicator = False

        self.hazard = False

        self.fuel = 100