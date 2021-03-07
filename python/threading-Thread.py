from threading import Thread
import time

start = time.perf_counter()


def do_something(name):
    time.sleep(1)
    print(f"Thread {name} Done Sleeping")


threads = []

for i in range(10):
    t = Thread(target=do_something, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()

finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
