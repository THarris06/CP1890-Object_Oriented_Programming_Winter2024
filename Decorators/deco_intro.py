# def f1():
#     print("Called f1")
#
#
# def f2(f):
#     f()
#
#
# f2(f1)

def f1(func):
    def wrapper(*args, **kwargs):
        print("started")
        func(*args, **kwargs)
        print("finished")
    return wrapper


@f1
def f(a):
    print(a)


@f1
def f3():
    print("hello f3")
# print(f1(f))
# f1(f)()

# x = f1(f)
# x()


f("hello")
# f3()
