from multiprocessing import Queue, Process, Manager
import os, time

# 队列的基本使用
# q = Queue(3)  # 设置一个大小为 3 的队列, 如果不写则没有上限
# print(q.qsize())  # 打印queue的大小, 为 0
#
# q.put("hello world")
# q.put("hello world-2")
# q.put("hello world-3")
#
# print(q.get())  # FIFO  先进先出
# print(q.qsize())

def write(q):
    for value in ["A", "B", "C"]:
        print("Put %s into the queue..."%value)
        q.put(value)
        time.sleep(1)

def read(q):
    while True:
        if not q.empty():
            value = q.get()
            print("Get %s from the queue..." % value)
            time.sleep(1)
        else:
            break

# 进程间通信
if __name__ == "__main__":
    que = Queue()
    pwrite = Process(target=write, args=(que,))
    pread = Process(target=read, args=(que,))
    # 启动写入内容的子进程
    pwrite.start()
    # 等待pwrite进程结束
    pwrite.join()
    # 读取之前写入的程序
    pread.start()
    pwrite.join()

    print("end")

    # que = Manager().Queue()  进程池之间进行通信
    # po = pool()
    # po.apply(write, (q,))
    # po.apply(read, (q,))
    # po.close()
    # po.join()