# Import threading to make do\_job() each process done in multi-thread
  - also import time.sleep for testing the run time
```
import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")
```
# Thread.start() to start process in a thread
  - In main(), use for loop to append each job to thread[] and then start the job
```
def main():
    thread = []
    for i in range(5):
        thread.append(threading.Thread(target = do_job,
                                       args=(i,)))
```

