"""
AUTOSAR Software Component Base Class
"""

from autosar.rte import rte


class SoftwareComponent:

    def __init__(self, name):

        self.name = name

    def write(self, signal, value):

        rte.write_signal(signal, value)

    def read(self, signal):

        return rte.read_signal(signal)