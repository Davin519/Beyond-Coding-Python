import threading
import time

class Worker(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        print(f"thread {self.n} start")
        time.sleep(2)
        print(f"thread {self.n} end")

startTime = time.time()

threads = []
print("main thread start")


for i in range(4):
    t = Worker(i)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("main thread end")
print(time.time() - startTime)