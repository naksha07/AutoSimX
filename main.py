"""
AutoSimX
Virtual AUTOSAR ECU Communication Simulator
"""

from communication.can_bus import CANBus

from ecu.engine_ecu import EngineECU
from ecu.cluster_ecu import ClusterECU
from ecu.body_ecu import BodyECU
from ecu.gateway_ecu import GatewayECU


def main():

    bus = CANBus()

    engine = EngineECU()
    cluster = ClusterECU()
    body = BodyECU()
    gateway = GatewayECU()

    bus.register_ecu(engine)
    bus.register_ecu(cluster)
    bus.register_ecu(body)
    bus.register_ecu(gateway)

    engine.simulate_drive()


if __name__ == "__main__":
    main()