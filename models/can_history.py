"""
Stores live CAN messages for the dashboard.
"""

from collections import deque


class CANHistory:

    def __init__(self):

        self.frames = deque(maxlen=500)

    def add(self, frame):

        self.frames.append(frame)

    def get(self):

        return list(self.frames)


history = CANHistory()