from datetime import datetime


def calcTime(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        timing = end - start
        print(timing)

    return wrapper


@calcTime
def test():
    sum = 0
    for i in range(1000000000):
        sum += i
    print(sum)


test()
