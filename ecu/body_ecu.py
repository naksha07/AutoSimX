from ecu.ecu import ECU

from communication.message_ids import (
    ENGINE_STATUS,
    BODY_COMMAND,
    LOCK_DOORS,
    UNLOCK_DOORS,
    HEADLIGHT_ON,
    HEADLIGHT_OFF,
    LEFT_INDICATOR,
    RIGHT_INDICATOR,
    HAZARD,
)

from models.global_state import vehicle


class BodyECU(ECU):

    def __init__(self):

        super().__init__("Body ECU")

    def receive(self, frame):

        self.frames_received += 1

        # Automatic headlights based on speed
        if frame.can_id == ENGINE_STATUS:

            speed = frame.data[0]

            vehicle.headlights = speed > 60

            print(
                f"[Body ECU] Headlights : "
                f"{'ON' if vehicle.headlights else 'OFF'}"
            )

        # GUI commands
        elif frame.can_id == BODY_COMMAND:

            command = frame.data[0]

            if command == LOCK_DOORS:

                vehicle.door_locked = True
                print("[Body ECU] Doors Locked")

            elif command == UNLOCK_DOORS:

                vehicle.door_locked = False
                print("[Body ECU] Doors Unlocked")

            elif command == HEADLIGHT_ON:

                vehicle.headlights = True
                print("[Body ECU] Headlights ON")

            elif command == HEADLIGHT_OFF:

                vehicle.headlights = False
                print("[Body ECU] Headlights OFF")

            elif command == LEFT_INDICATOR:

                vehicle.left_indicator = not vehicle.left_indicator
                print("[Body ECU] Left Indicator")

            elif command == RIGHT_INDICATOR:

                vehicle.right_indicator = not vehicle.right_indicator
                print("[Body ECU] Right Indicator")

            elif command == HAZARD:

                vehicle.hazard = not vehicle.hazard
                print("[Body ECU] Hazard Lights")