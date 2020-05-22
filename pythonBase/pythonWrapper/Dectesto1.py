import logging

# 函数装饰器
def user_logging1(func):
    print("@user_logging1")
    def wrapper(*args, **kwargs):
        logging.info("%s is running.."% func.__name__)
        print("wrapper1 inner.....")
        return func(*args)

    return wrapper

def user_logging2(func):
    print("@user_logging2")
    def wrapper(*args, **kwargs):
        logging.info("%s is running.."% func.__name__)
        print("wrapper2 inner.....")
        return func(*args)

    return wrapper

@user_logging1
@user_logging2
def bar():
    print("i am bar....")

# 类装饰器
class Foo():

    def __init__(self, func):
        print("class foo")
        self._func = func
    
def __call__(self):
    print("class decorator runnig.....")
    self._func()
    print("class decoraton ending.....")

@Foo
def classFoo():
    print("class foo...")


# 装饰器实例3
def log_with_param(test):
    def decoration(func):
        def wrapper(*args, **kwargs):
            print('call %s():' %func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(test))
            return func(*args, **kwargs)
        return wrapper
    return decoration


@log_with_param("param")
def test_with_param(p):
    print("p: ",p)
    print("func name: ",test_with_param.__name__)



if __name__ == "__main__":
    bar()
    f = Foo(classFoo)
    test_with_param("i am xhaoge")