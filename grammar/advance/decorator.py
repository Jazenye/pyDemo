#coding=utf-8

def foo():
    print("-- function foo --")

print(foo)  # 这个foo 指向了一个函数体

b = foo  # 这个类似C中的函数指针，python中就可以直接调用
print(b)

b()

# 闭包
def  closure(num1, num2):
    def test(num):
        return(num*num1 + num2)

    return test  # different from: return test()

line = closure(2, 2)  # y = kx + b , 这里指定了k & b
print(line(5))  # print(closure(2, 2)(5))

# 装饰器
def outter(fun):
    def inner():
        print("-- inner --")
        fun()
    return inner

def foo():
    print("-- foo --")

@outter
def foo2():
    print("-- foo 222 --")

foo = outter(foo)  # 装饰器的原理
foo()
foo2()

# 多个装饰器的装饰调用顺序
def bolder(fn):
    print("bolder 正在装饰")  # 不调用 即使是装饰也会执行
    def inner():
        print("-- bolder --")
        return "<b>" + fn() + "</b>"
    return  inner

def italic(fn):
    print("italic 正在装饰")
    def inner():
        print("-- italic --")
        return "<i>" + fn() + "</i>"
    return inner

# 调用的顺序是从上往下， 但装饰的顺序 是从下往上.
@bolder
@italic
def content():
    return "Hello World"

print(content() )  # bolder  italic   <b><i>Hello World</i></b>

# 不定长参数的传递
def testArg(fun):
    def inner(*args, **kwargs):
        ret =  fun(*args, **kwargs)  # 传递具有返回值的函数
        return ret
    return inner

@testArg
def tests(a, b, c, d):
    return (a+b+c+d)

print(tests(1, 2, 3, 4))


# 带参数的装饰器, 为了能让在运行时拥有不同的功能
def dec_arg(arg):
    print("-- 装饰器传入了参数，执行外层函数 --")

    def middle(fun):
        print("-- @dec_arg, 装饰器装饰 --")

        def inner():
            if arg == "Hello world":
               fun()
            else:
                print("Error")
        return inner

    return middle

@dec_arg("Hello world")
def bar():
    print("-- bar --")

bar()
