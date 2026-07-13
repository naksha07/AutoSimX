"""
AutoSimX
Virtual AUTOSAR ECU Communication Simulator
"""

from communication.can_frame import CANFrame
from ecu.ecu import ECU


def main():

    engine = ECU("Engine ECU")

    body = ECU("Body ECU")

    frame = CANFrame(
        can_id=0x100,
        sender="Engine ECU",
        receiver="Body ECU",
        data=[1]
    )

    engine.send(frame)

    body.receive(frame)


if __name__ == "__main__":
    main()