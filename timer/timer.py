# a simple class to record time taken for something to complete
import time
import logging
from json import dumps
from kafka import KafkaProducer


class Stopwatch(object):
    """
    A class that can be wrapped around a function using a 'with' statement to record the time taken for the operation within to complete

    """

    def __init__(self, print_time=True):
        logging.basicConfig(
            level=logging.INFO,
            datefmt="%d/%m/%Y %I:%M:%S %p",
            format="[%(asctime)s] %(levelname)s: %(message)s",
        )
        self.print_time = print_time
        self.start = 0
        self.time_taken = 0

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, *args):
        self.time_taken = time.perf_counter() - self.start
        if self.print_time:
            logging.info(f"Time taken to complete operations: {self.time_taken}s")


class StopwatchKafka(Stopwatch):
    """
    A subclass of the Stopwatch class that has additional functionalities for sending data to a Kafka topic via the Kafka Producer
    """

    def __init__(
        self,
        print_time=True,
        bootstrap_servers=["localhost:9092"],
    ):
        super().__init__(print_time)
        self.bootstrap_servers = bootstrap_servers

    def __enter__(self):
        super().__enter__()

    def __exit__(self, *args):
        super().__exit__()
        logging.info(self.time_taken)
