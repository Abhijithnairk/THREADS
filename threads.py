import time
import threading

start = time.perf_counter()

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    print("done sleeping")
    
threads = []
for i in range(10):
    t = threading.Thread(target=do_something)
#   t2 = threading.Thread(target=do_something)
    t.start()
#   t2.start()
    threads.append(t)
for thread in threads:
    thread.join()
#  t2.join()

finish = time.perf_counter()

print(f"Finished in: {round(finish-start,2)}")

