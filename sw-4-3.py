from datetime import datetime
from time import sleep

for i in range(5):
    date = datetime.now()
    print(date.time())
    sleep(1)