from multiprocessing import Pool
import os
import time

def worker(num):
    for i in range(3):
        print("--- pid = %d,  i = %d"%(os.getpid(), i))
        time.sleep(1)

if __name__ == "__main__":
    p = Pool(3)
    for i in range(4):
        print("*** %d ***" % i)
        # 如果添加的任务数量超过进程池容量， 会等待进程池中的任务完成后再填充新的替代
        p.apply_async(worker, (i,))  # or args=(i,) 这里拿走了任务
        # p.apply() 同步的方法， 不过一般不用

    p.close()  # 关闭进程池， 且必须在join()之前
    p.join()  # 主进程默认不会等待进程池中的任务完成结束,而继续完成主进程
    # 没有join() 会导致子进程中的任务不会执行