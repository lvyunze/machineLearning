from datetime import datetime
import time
import random
from concurrent.futures import ProcessPoolExecutor, wait
from public import timer


def fun(a):
    print(a)


@timer
def run():
    pool_size = 1
    pool = ProcessPoolExecutor(pool_size)
    tasks = [pool.submit(fun, i) for i in range(10000)]
    wait(tasks)
    print("done")


if __name__ == '__main__':
    run()