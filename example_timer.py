from timer.timer import StopwatchKafka
import time

timer = StopwatchKafka(True)

with timer:
    for x in range(5):
        time.sleep(1)
        print(x)
