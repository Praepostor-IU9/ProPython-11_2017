import time
from functools import wraps


def log_duration(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        print(time.time() - t1)
        return res

    return new_func


@log_duration
def time_sleep(a):
    time.sleep(a)
    return 'Ok'


print(time_sleep(1))
print(time_sleep.__name__)
