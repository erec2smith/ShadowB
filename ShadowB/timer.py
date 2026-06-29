import time

class Timer:
    def __init__(self):
        self._start_time = None
        
    def start(self):
        self._start_time = time.perf_counter()
        
    def stop(self):
        if self._start_time is None:
            raise RuntimeError("Timer has not been started!")
        
        elapsed = time.perf_counter() - self._start_time
        self._start_time = None
        return elapsed
    
    def reset(self):
        self._start_time = time.perf_counter()
        
timer = Timer()

def start():
    return timer.start()

def stop():
    return timer.stop()

def reset():
    return timer.reset()