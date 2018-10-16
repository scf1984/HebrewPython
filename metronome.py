# get bpm
# Play a beep once every 60/bpm seconds

import winsound
import time

bpm = 120
weight = 3
dt = 60 / bpm
i = 0
try:
    start_time = time.time()
    while True:
        winsound.Beep(880 if i % weight == 0 else 440, 250)
        i += 1
        time_elapsed = start_time - time.time()
        time.sleep(time_elapsed % dt)
except KeyboardInterrupt:
    print('Goodbye!')
