import threading
import time

def theradingRun(n):
    print("\ntask: ",n)
    time.sleep(1)
    print("\n",n," sleep: 1s")
    time.sleep(2)
    print("\n",n," sleep: 2s")


if __name__ == "__main__":
    t1 = threading.Thread(target=theradingRun, args=("t1",))
    t2 = threading.Thread(target=theradingRun, args=("t2",))
    t3 = threading.Thread(target=theradingRun, args=("t4",))
    t1.start()
    t2.start()
    t3.start()