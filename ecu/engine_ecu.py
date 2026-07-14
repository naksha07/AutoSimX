"""
Engine ECU
Simulates engine speed and RPM and broadcasts Engine Status over CAN.
"""

import time

from ecu.ecu import ECU
from communication.can_frame import CANFrame
from communication.message_ids import ENGINE_STATUS
from models.global_state import vehicle

from models.dtc_manager import dtc_manager
from diagnostics.dtc_codes import (
    LOW_FUEL,
    ENGINE_OVERHEAT,
)

from autosar.engine_component import EngineComponent


class EngineECU(ECU):

    def __init__(self):
        super().__init__("Engine ECU")
        self.swc = EngineComponent()

    def simulate_drive(self):

        # Accelerate
        for speed in range(0, 101, 20):

            rpm = 800 + speed * 25

            # Update shared vehicle state
            vehicle.speed = speed
            vehicle.rpm = rpm

            vehicle.fuel -= 2
            vehicle.engine_temperature += 3

            if vehicle.fuel <= 15:
                dtc_manager.add(LOW_FUEL)

            if vehicle.engine_temperature >= 120:
                dtc_manager.add(ENGINE_OVERHEAT)

            self.swc.update(speed, rpm)

            frame = CANFrame(
                can_id=ENGINE_STATUS,
                sender=self.name,
                data=[speed, rpm // 100]
            )

            self.send(frame)

            time.sleep(1)

        # Decelerate
        for speed in range(80, -1, -20):

            rpm = 800 + speed * 25

            vehicle.speed = speed
            vehicle.rpm = rpm

            vehicle.fuel -= 2
            vehicle.engine_temperature += 3

            if vehicle.fuel <= 15:
                dtc_manager.add(LOW_FUEL)

            if vehicle.engine_temperature >= 120:
                dtc_manager.add(ENGINE_OVERHEAT)

            self.swc.update(speed, rpm)

            frame = CANFrame(
                can_id=ENGINE_STATUS,
                sender=self.name,
                data=[speed, rpm // 100]
            )

            self.send(frame)

            time.sleep(1)

        print("\n========== Drive Cycle Complete ==========")