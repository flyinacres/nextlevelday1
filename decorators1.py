def printlog(func):
    def wrapper(arg):
        print("CALLING: " + func.__name__)
        return func(arg)
    return wrapper
@printlog
def f(n):
    return n + 2

print(f(3))