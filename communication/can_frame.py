"""
CAN Frame Module
Represents a standard CAN message.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CANFrame:
    """
    Represents a virtual CAN Frame.
    """

    can_id: int
    sender: str
    receiver: str
    data: list[int]

    timestamp: datetime = field(default_factory=datetime.now)

    @property
    def dlc(self) -> int:
        """Data Length Code"""
        return len(self.data)

    def display(self):
        """Print CAN Frame information."""

        print("=" * 45)
        print("CAN FRAME")
        print("=" * 45)
        print(f"Time      : {self.timestamp}")
        print(f"CAN ID    : {hex(self.can_id)}")
        print(f"Sender    : {self.sender}")
        print(f"Receiver  : {self.receiver}")
        print(f"DLC       : {self.dlc}")
        print(f"Data      : {self.data}")
        print("=" * 45)