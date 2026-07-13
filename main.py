from communication.can_bus import CANBus

from ecu.engine_ecu import EngineECU
from ecu.cluster_ecu import ClusterECU
from ecu.body_ecu import BodyECU
from ecu.gateway_ecu import GatewayECU

from scheduler.task_scheduler import TaskScheduler


def main():

    print("=" * 60)
    print("        AutoSimX - Automotive ECU Simulator")
    print("=" * 60)

    # Create CAN Bus
    bus = CANBus()

    # Create ECUs
    engine = EngineECU()
    cluster = ClusterECU()
    body = BodyECU()
    gateway = GatewayECU()

    # Register ECUs
    bus.register_ecu(engine)
    bus.register_ecu(cluster)
    bus.register_ecu(body)
    bus.register_ecu(gateway)

    # Create Scheduler
    scheduler = TaskScheduler()

    # Add ECU Tasks
    scheduler.add_task(engine.simulate_drive)

    # Start all tasks
    scheduler.start()

    # Wait for all tasks to finish
    scheduler.wait()


if __name__ == "__main__":
    main()