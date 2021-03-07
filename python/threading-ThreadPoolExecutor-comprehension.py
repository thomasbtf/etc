from concurrent.futures import ThreadPoolExecutor, as_completed
import time

start = time.perf_counter()


def do_something(seconds):
    print(f"Sleeping for {seconds} second(s)")
    time.sleep(seconds)
    return f"Done Sleeping ... {seconds}"


with ThreadPoolExecutor() as executor:
    secs = [5, 4, 3, 2, 1]

    # this returns future objects!
    submits = [executor.submit(do_something, sec) for sec in secs]

    for submit in as_completed(submits):
        print(submit.result())


finish = time.perf_counter()

print(f"Finished in {round(finish-start, 2)} second(s)")
