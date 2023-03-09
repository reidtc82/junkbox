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

#executors will connect to the driver through a socket and add themselves to the executor list in doing so

from enum import Enum
from multiprocessing import Process

class State(Enum):
    stopped = 1
    running = 2
    paused = 3


class Driver:
    def __init__(self, ip_address, listener_port, port_range):
        self.job_queue = []
        self.result_queue = []
        self.executors = []
        self.ip_address = ip_address
        self.listener_port = listener_port
        self.port_range = port_range
        self.state = State.stopped
    
    def socket_listener(self):
        # listen for new executors
        # add them to the executor list
        # IP address for the driver and the listener port should be passed in the construction of the driver
        # if a handshake is made, this should select an unclaimed port from the port range and 
        # pass the session to the socket function
        while self.state == State.running:
            # listen for new connections
            # if a connection is made, pass it to the socket function
            pass

    def socket(self, port):
        # create a socket connection to the executor
        # the socket_listener will listen for connections, if it receives one it will pass that work to this socket

    def stop_listener(self):
        # stop the socket listener
        self.state = State.stopped
    
    def start_listener(self):
        # start the socket listener
        self.state = State.running
    
    def pause_listener(self):
        # pause the socket listener
        self.state = State.paused
    
    def run(self):
        # start the socket listener
        # start the job queue
        # start the result queue
        # use the multiprocessing module to run the socket listener and the job queue in separate processes
        listener = Process(target=self.socket_listener)
        listener.start()
        job_queue = Process(target=self.job_queue)
        job_queue.start()
        result_queue = Process(target=self.result_queue)
        result_queue.start()
