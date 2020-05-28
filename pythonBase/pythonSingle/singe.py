'''
单例是一种设计模式，应用该模式的类只会生成一个实例。
单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：
如果实例不存在，会创建一个实例；如果已存在就会返回这个实例。
因为单例是一个类，所以你也可以为其提供相应的操作方法，以便于对这个实例进行管理。'''

# 创建单例模式的N种方式
# 使用装饰器，维护一个字段对象instances，缓存所有的单例类，只要单例不存在就创建，已经存在了就直接返回该实例对象

def singleton(cls):
    isinstance = {}
    def wrapper(*args,**kwargs):
        if cls not in isinstance:
            isinstance[cls] = cls(*args,**kwargs)
        return isinstance[cls]
    return wrapper

@singleton
class Foo():
    def __init__(self):
        pass


# 使用基类，__new__ 是真正创建实例对象的方法，重写基类的__new__方法，以此来保证创建对象的时候只生成一个实例

class SingletonNew():
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonNew, cls).__new__(cls, *args,**kwargs)
        return cls._instance

    def __init__(self):
        pass
    
class Foo1(SingletonNew):
    pass


# 使用元类，元类是用于创建对象的类，类对象创建实例对象时一定会调用__call__方法，因此在调用__call__方法时保证只创建一个实例即可，type时python中的一个元类

class SingletonCall():
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(SingletonCall, cls).__call__(cls, *args,**kwargs)
        return cls._instance

class Foo2(SingletonCall):
    __metaclass__ = SingletonCall



if __name__ == "__main__":
    c1 = Foo()
    c2 = Foo()
    print(id(c1) == id(c2))



