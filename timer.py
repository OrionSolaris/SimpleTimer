# a simple class to record time taken for something to complete
import time


class Stopwatch(object):
    """
    A class that can be wrapped around a function using a 'with' statement to record the time taken for the operation within to complete

    """

    def __init__(self, print_time=True):
        self.print_time = print_time
        self.start = 0
        self.time_taken = 0

    def __enter__(self):
        self.start = time.perf_counter()

    def __exit__(self, *args):
        self.time_taken = time.perf_counter() - self.start
        if self.print_time:
            print(f"Time taken to complete operations: {self.time_taken}s")
