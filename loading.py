import time
import sys


animation = "|/⎯\|"
for i in range(50):
    time.sleep(0.1)
    sys.stdout.write("\r" + "Waiting " + animation[i % len(animation)])
    sys.stdout.flush()
    #do something
