import abc


class Worker(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def work():
        pass


class StandWorker(Worker):
    @staticmethod
    def work():
        print("I'm working!!")


class SuperWorker(Worker):
    @staticmethod
    def work():
        print("I work very hard!!!")


class Manager:

    def __init__(self):
        self.worker = None

    def set_worker(self, worker_):
        assert isinstance(worker_, Worker), f"`worker` must be of type {Worker}"
        self.worker = worker_

    def manage(self):
        if self.worker is not None:
            self.worker.work()


worker = StandWorker()
manager = Manager()
manager.set_worker(worker)
manager.manage()

super_worker = SuperWorker()
try:
    manager.set_worker(super_worker)
    manager.manage()
except AssertionError:
    print("manager fails to support super_worker....")
