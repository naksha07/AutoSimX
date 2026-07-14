from models.dtc_manager import dtc_manager
from diagnostics.dtc_codes import *

dtc_manager.add(ENGINE_OVERHEAT)
dtc_manager.add(LOW_FUEL)
dtc_manager.add(CAN_BUS_OFF)

print()

for dtc in dtc_manager.get():

    print(dtc)