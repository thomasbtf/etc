from concurrent.futures import ThreadPoolExecutor
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping ... {seconds}"


with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # this returns the return in the order the thread was started
    # Exceptions wont be raised here
    results = executor.map(do_something, secs)

    # Exceptions are raised here
    for result in results:
        print(result)

    # Threads will be joined here, before context manager finished


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
