import time

start = time.perf_counter()

def do_something():
    print("sleeping 1 second")
    time.sleep(1)
    print("done sleeping")
    
for i in range(10):    
    do_something()

finish = time.perf_counter()

print(f"Finished in: {round(finish-start,2)}")