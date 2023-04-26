import time


def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        elapsed_time = (time.time() - start) / 60
        print(f"Elapsed time: {elapsed_time:.2f} minutes")
        return result

    return wrapper
