"""
Stores live CAN messages for the dashboard.
"""

from collections import deque


class CANHistory:

    def __init__(self):
        self.frames = []

    def add(self, frame):
        self.frames.append(frame)

        if len(self.frames) > 200:
            self.frames.pop(0)

    def get(self):
        return self.frames


history = CANHistory()