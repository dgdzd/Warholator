import time

def get_performance(func, *args, **kwargs) -> tuple[float, any]:
    start = time.time()
    ret = func(*args, **kwargs)
    return (time.time() - start, ret)