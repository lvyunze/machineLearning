import time


def timer(func):
    def wrapper(*args, **kwargs):
        time_start = time.time()
        res = func(*args, **kwargs)
        cost_time = time.time() - time_start
        print(f"运行时长为：{cost_time}")
        return res
    return wrapper
