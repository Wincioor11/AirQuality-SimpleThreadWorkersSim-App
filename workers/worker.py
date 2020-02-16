import threading


class Worker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.lock = threading.Lock()
        self.run_flag = True

    def run(self):
        pass

    def stop(self):
        self.run_flag = False
