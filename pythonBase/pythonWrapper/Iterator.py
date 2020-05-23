'''
迭代器就是用于迭代操作for循环的对象，像列表一样可以迭代其中的每一个元素，任何实现了__next__方法的对象都可以称为迭代器
与列表的区别：不像列表一样一次性加载所有的参数到内存，而是以一张弓延迟计算方式返回元素'''


# 以斐波那契数列为例来实现一个迭代器
class Fib:

    def __init__(self, n):
        self.prev = 0
        self.cur = 1
        self.n = n
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.n > 0:
            value = self.cur
            self.cur = self.cur + self.prev
            self.prev = value
            self.n -= 1
            return value
        else:
            raise StopIteration()

'''
生成器是一种函数，使用yield来返回值，函数调用时返回一个生成器对象，本质上是一个迭代器，只是更加简洁'''


def fib(n):
    prev, curr = 0,1
    while n>0:
        n -= 1
        yield curr
        prev, curr = curr, curr+prev




if __name__ == "__main__":
    f = Fib(10)
    print(f)
    print(next(f))
    print([i for i in f])

    print("------------生成器表达式------------")
    print([i for i in (x**2 for x in range(5))])    

