"""
AUTOSAR Runtime Environment (RTE)
"""

class RuntimeEnvironment:

    def __init__(self):

        self.signals = {}

    def write_signal(self, signal_name, value):

        self.signals[signal_name] = value

    def read_signal(self, signal_name):

        return self.signals.get(signal_name)

    def clear(self):

        self.signals.clear()


rte = RuntimeEnvironment()