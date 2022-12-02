from timer import Stopwatch
import time

timer = Stopwatch(True)

with timer:
    for x in range(5):
        time.sleep(1)
        print(x)
