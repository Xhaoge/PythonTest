#确定某个字符串内是否有唯一的字符，返回bool
def hasUniquaString(str):
    if str is None:
        return False
    return len(set(str)) == len(str)

#整除返回
def fizzBuzz(num):
    if num is None or num <1:
        raise "number is error"
    result = []
    for i in range(1, num+1):
        if i % 3 == 0 and i % 5== 0 :
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
s = map(lambda x:x*2,[1,2,3,4,5])
print(list(s))