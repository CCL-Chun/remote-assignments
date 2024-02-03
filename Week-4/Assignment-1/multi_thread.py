import threading
from time import sleep

def do_job(number):
    sleep(3)
    print(f"Job {number} finished")

# rewrite everything inside this main function and keep others untouched
def main():
    thread = []
    for i in range(5):
        thread.append(threading.Thread(target = do_job,
                                       args=(i,)))
        thread[i].start()
    for i in range(5):
        thread[i].join()

main()

##test
#import time
#start = time.time()
#main()
#end = time.time()
#print(end - start)