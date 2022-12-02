from timer.timer import StopwatchKafka

import time

timer = StopwatchKafka(kafka_topic="numtest")


for x in range(5):
    with timer:
        time.sleep(2)
