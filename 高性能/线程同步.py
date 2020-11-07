# import threading
# import time
#
#
# def thread():
#     time.sleep(2)
#     print('---子线程结束---')
#
#
# def main():
#     t1 = threading.Thread(target=thread)
#     t1.start()
#     print('---主线程--结束')
#
#
# if __name__ == '__main__':
#     main()


import threading
import time
import random

# 同步两个不同线程，信号量被初始化0
semaphore = threading.Semaphore(0)


def consumer():
    print("-----等待producer运行------")
    semaphore.acquire()  # 获取资源，信号量为0被挂起，等待信号量释放
    print("----consumer 结束----- 编号: %s" % item )


def producer():
    global item  # 全局变量
    time.sleep(3)
    item = random.randint(0, 100)  # 随机编号
    print("producer运行编号: %s" % item)
    semaphore.release()


if __name__ == "__main__":
    for i in range(0, 50):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("程序终止")