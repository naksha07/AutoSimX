"""
Diagnostic Trouble Code Manager
"""

from datetime import datetime

from diagnostics.dtc_codes import DTC_DESCRIPTION


class DTCManager:

    def __init__(self):

        self.active = []

    def add(self, code):

        for dtc in self.active:

            if dtc["code"] == code:
                return

        self.active.append({

            "code": code,

            "description": DTC_DESCRIPTION.get(
                code,
                "Unknown Fault"
            ),

            "time": datetime.now()

        })

        print(f"[DTC] {code} Registered")

    def clear(self):

        self.active.clear()

        print("[DTC] All DTCs Cleared")

    def get(self):

        return self.active

    def has_faults(self):

        return len(self.active) > 0


dtc_manager = DTCManager()