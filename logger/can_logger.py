import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/can.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s",
)


def log_frame(frame):

    logging.info(
        f"{hex(frame.can_id)} | "
        f"{frame.sender} | "
        f"{frame.data}"
    )