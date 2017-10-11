from multiprocessing import Process
import os
import time

class MyNewProcess(Process):
    # 重写run方法, 调用p.start()的时候自动调用
    def run(self):
        for i in range(5):
            print("--- ", i)
            time.sleep(1)


def run_pro(name):
    print("Run child process %s ( %s )" % (name, os.getpid()))

if __name__ == "__main__":
    print("Parent process %s." % os.getpid())
    p = Process(target=run_pro, args=("test",))  # 跨平台的模块， 创建一个进程 传参 返回
    print("Child process will start")
    p.start()  # 启动这个进程
    # p.terminate()  直接结束子进程
    p.join(1)  # 等到子进程结束, 可选参数: 如果1s 内子进程未结束就提前结束
    print("Child process end")

    p2 = MyNewProcess()  # 第二种创建进程的方式
    print("--- new process ---")
    p2.start()
