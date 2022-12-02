from timer import Stopwatch
import time

timer = Stopwatch()

with timer:
    for x in range(10):
        time.sleep(1)
        print(x)
