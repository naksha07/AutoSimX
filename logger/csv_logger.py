import csv
import os


class CSVLogger:

    def __init__(self):

        self.filename = "logs/can_log.csv"

        os.makedirs("logs", exist_ok=True)

        if not os.path.exists(self.filename):

            with open(self.filename, "w", newline="") as file:

                writer = csv.writer(file)

                writer.writerow([
                    "Timestamp",
                    "CAN ID",
                    "Sender",
                    "DLC",
                    "Data"
                ])

    def log(self, frame):

        with open(self.filename, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                frame.timestamp.strftime("%H:%M:%S.%f")[:-3],
                hex(frame.can_id),
                frame.sender,
                frame.dlc,
                " ".join(f"{b:02X}" for b in frame.data)
            ])


csv_logger = CSVLogger()