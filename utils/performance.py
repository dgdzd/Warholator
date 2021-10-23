import time

class Performance:
    def __init__(self, begin: float, end: float):
        self.begin = begin
        self.end = end
    
    def get_execution_time(self):
        return self.end - self.begin

def get_performance(func, *args, **kwargs) -> tuple[Performance, any]:
    start = time.time()
    ret = func(*args, **kwargs)
    return (Performance(start, time.time()), ret)