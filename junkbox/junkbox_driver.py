# Junkbox driver that manages the execution of jobs
# executors form a distributed mesh network
# the driver will send jobs to the executors
# the executors will execute the jobs
# the executors will return the results to the driver
# the driver will manage the execution of jobs

# The driver communicates with the executors using a socket connection
# the driver maintains a job queue and a result queue
# It will monitor the heartbeat of the executor and if it fails it will remove it from the mesh network
# If the driver removes a node from the mesh network it will reassign the jobs that were assigned to that node
# that means teh executor needs to be able to handle the reassignment of jobs
# and that it can track which jobs are assigned to which executors

# The driver is passed to the Math class
# The Math class will use the driver to execute jobs
# The Math class will return the results to the user

# The math class will give the driver a list of cells to be executed
# those cell smay be a single cell or a JunkBox object
# the math class wil also pass the function to perform on each

# executors will connect to the driver through a socket and add themselves to the executor list in doing so

from multiprocessing import Process
import asyncio


class State:
    STOPPED = 1
    RUNNING = 2
    PAUSED = 3


class JunkBoxPool:
    def __init__(self):
        self._state = State.STOPPED
        self.processes = []

    def __enter__(self):
        self._state = State.RUNNING
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._state = State.STOPPED

    def apply_async(self, target, args) -> str:
        if self._state == State.RUNNING:
            result = None

            def internal_target(*args):
                result = target(*args)

            process = Process(target=internal_target, args=(result, args))
            self.processes.append(process)
            process.start()
            yield result

    def map(self, func, args):
        if self._state == State.RUNNING:
            for arg in args:
                process = Process(target=func, args=arg)
                self.processes.append(process)
                process.start()
                yield process

    def join(self, timeout=None):
        for process in self.processes:
            process.join(timeout=timeout)

    def get(self):
        results = []
        for process in self.processes:
            results.append(process)
        return results
