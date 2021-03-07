from multiprocessing import cpu_count
from joblib import Parallel, delayed
from tqdm import tqdm


def some_functions(entry):
    # do something

    return entry


if __name__ == "__main__":
    some_iterable = []
    num_cores = cpu_count()

    results = []

    results = Parallel(n_jobs=num_cores)(
        delayed(some_functions)(entry) for entry in tqdm(some_iterable)
    )
