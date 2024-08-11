import time
import os

cls = lambda: os.system('cls')

seconds = 31536000

for x in range(seconds, -1, -1):

    s = x % 60
    m = int(x / 60) % 60
    h = int(x / 3600) % 24
    d = int(x / 86400) % 365
    y = int(x / 31536000)

    print(f"{y:02}:{d:02}:{h:02}:{m:02}:{s:02}")
    time.sleep(1)
    cls()

print("The year is over!!!")
