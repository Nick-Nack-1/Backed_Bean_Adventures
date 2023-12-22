import time

class timer():
    def __init__(self):
        self.start = time.perf_counter()
        self.time = 0
    

    def stop(self):
        self.time = time.perf_counter()-self.start
        if self.time > 0.018:
            print(self.time)
        else:
            print(".")
        self.start = time.perf_counter()