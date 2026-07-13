import logging

logging.basicConfig(

    filename="logs/can.log",

    level=logging.INFO,

    format="%(asctime)s | %(message)s"
)


def log(frame):

    logging.info(

        f"{hex(frame.can_id)} "

        f"{frame.sender} "

        f"{frame.data}"
    )