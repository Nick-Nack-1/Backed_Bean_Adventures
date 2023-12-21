import time

class timer():
    def __init__(self):
        self.start = time.perf_counter()
    

    def stop(self):
        print(time.perf_counter()-self.start)