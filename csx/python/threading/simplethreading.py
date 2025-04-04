from threading import Thread
from time import sleep

class Work(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(5):
            print(f"{self.name} is working...")
            sleep(1)


work1 = Work("Thread 1")
work2 = Work("Thread 2")

work1.start()
work2.start()

work1.join()
work2.join()

print("All threads have finished.")