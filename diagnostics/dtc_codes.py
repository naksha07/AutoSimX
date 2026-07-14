"""
Standard Diagnostic Trouble Codes
"""

ENGINE_OVERHEAT = "P0217"
LOW_FUEL = "P0463"
ENGINE_TIMEOUT = "U0100"
CAN_BUS_OFF = "U0001"
HEADLIGHT_FAILURE = "B2575"
DOOR_LOCK_FAILURE = "B1001"
SPEED_SENSOR_FAILURE = "P0500"

DTC_DESCRIPTION = {

    ENGINE_OVERHEAT:
        "Engine Over Temperature",

    LOW_FUEL:
        "Fuel Level Sensor Circuit High",

    ENGINE_TIMEOUT:
        "Lost Communication With Engine ECU",

    CAN_BUS_OFF:
        "CAN Bus Communication Failure",

    HEADLIGHT_FAILURE:
        "Headlight Circuit Failure",

    DOOR_LOCK_FAILURE:
        "Door Lock Actuator Failure",

    SPEED_SENSOR_FAILURE:
        "Vehicle Speed Sensor Failure",
}