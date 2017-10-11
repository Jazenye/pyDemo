#coding=utf-8

'''
    a = []
    for x in range(5):
        a.append(x*x)
'''
a = [x*x for x in range(5)]  # 用这种生成式一行解决了3行的代码
print(a)

b = (x*2 for x in range(4))  # 生成器的创建方式, 小括号  占用空间少
for i in range(4):
    print(next(b), end='   ')  # 与该方法等价： b.__next__()

try:
    next(b)
except StopIteration:
    print(" 已越界")


def createNum():
    a, b = 0, 1
    for i in range(5):
        temp = yield b  # 生成器的关键字, 运行到该处停止并返回yield后的b
        print(temp)  # yield b 返回值为 none
        a, b = b, a+b

a = createNum()  # 把a作为生成器对象
ret = next(a)
ret = next(a)
print(ret)
a.send("hello world")  # 把这个字符串作为返回值传给temp, 并执行a.__next__()

# multitask,
def task1():
    while True:
        print("-- 1 --")
        yield None

def task2():
    while True:
        print("-- 2 --")
        yield None

t1 = task1()
t2 = task2()
while True:
    t1.__next__()
    t2.__next__()