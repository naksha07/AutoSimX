"""
AutoSimX
Virtual AUTOSAR ECU Communication Simulator
"""

from communication.can_bus import CANBus
from communication.can_frame import CANFrame
from ecu.ecu import ECU


def main():

    can_bus = CANBus()

    engine = ECU("Engine ECU")
    body = ECU("Body ECU")
    cluster = ECU("Cluster ECU")

    can_bus.register_ecu(engine)
    can_bus.register_ecu(body)
    can_bus.register_ecu(cluster)

    frame = CANFrame(
        can_id=0x100,
        sender="Engine ECU",
        receiver="Body ECU",
        data=[1]
    )

    engine.send(frame)


if __name__ == "__main__":
    main()