"""
Simple Task Scheduler
"""

import threading


class TaskScheduler:

    def __init__(self):

        self.tasks = []

    def add_task(self, target):

        thread = threading.Thread(
            target=target,
            daemon=True
        )

        self.tasks.append(thread)

    def start(self):

        for task in self.tasks:

            task.start()

    def wait(self):

        for task in self.tasks:

            task.join()