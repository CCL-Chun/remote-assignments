# Import threading to make do\_job() each process done in multi-thread
  - import time.sleep for waiting time between process
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
                                       args=(i,))) #assign child threads for each work
```
# Thread.join() to make main thread work after all threads are done
  - if the main thread have to wait for all child threads done and continue
  - use join() here to count the run time
```
for i in range(5):
        thread[i].join()
```
## testing
```
import time
start = time.time() #main thread
main() #child threads
end = time.time() #main thread
print(end - start) #run time(also main thread)
#result
Job 2 finished
Job 3 finished
Job 0 finished
Job 1 finished
Job 4 finished
3.0060160160064697 #run time
```


