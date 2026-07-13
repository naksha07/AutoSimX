"""
CAN Logger
"""

import csv
import os

from models.can_history import history

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "can_log.csv")


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


if not os.path.exists(LOG_FILE):

    with open(LOG_FILE, "w", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                "Timestamp",
                "CAN_ID",
                "Sender",
                "DLC",
                "Data",
            ]
        )


def log_frame(frame):

    history.add(frame)

    with open(LOG_FILE, "a", newline="") as f:

        writer = csv.writer(f)

        writer.writerow(
            [
                frame.timestamp.strftime("%H:%M:%S.%f")[:-3],
                hex(frame.can_id),
                frame.sender,
                frame.dlc,
                " ".join(f"{x:02X}" for x in frame.data),
            ]
        )