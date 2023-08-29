import random
import socket
import sys
import threading
import time
<<<<<<< HEAD
import dill as pickle
from src.utility.math import MathPrimitives
from multiprocessing import Process, Queue
=======
import json
>>>>>>> origin/queuing

import dill as pickle

from src.utility.junk import Job, WorkRequest, WorkReturn
from src.utility.math import MathPrimitives


class JunkBoxServer:
    """A simple TCP server that listens for incoming connections and
    sends a response back to the client.
    """
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.is_running = False
        self.clients = dict()
        self.math_primatives = MathPrimitives()
<<<<<<< HEAD
        # create a multiprocessing interface for a shell to interact with the job queue

=======
        self.jobs = []
>>>>>>> origin/queuing

    def start(self):
        """Starts the server"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # run the sockets on one process and then start another to allow interaction with the job queue

            self.server_socket.bind((self.host, self.port))

            self.server_socket.listen(5)
            print("Server is running and listening for connections...")
            self.is_running = True

            while self.is_running:
                client_socket, client_address = self.server_socket.accept()

                client_thread = threading.Thread(
                    target=self.handle_client, args=(client_socket, client_address)
                )
                client_thread.start()

        except KeyboardInterrupt:
            print("Server shutdown initiated by keyboard interrupt...")
            self.stop()
            sys.exit(1)
        except Exception as exception:
            print("An error occurred:", str(exception))
            self.stop()
            sys.exit(1)

    def handle_client(self, client_socket, client_address):
        """Handles a client connection"""
        print("Connected to:", client_address)
        self.clients[client_address] = client_socket

        while True:
            data = client_socket.recv(1024)
            data = pickle.loads(data)

            if not data:
                print("No data...")
                break

            if client_socket.fileno() != -1:  # -1 means an error occurred
                if data["header"] == "work_request":
<<<<<<< HEAD
                    time.sleep(random.randint(1, 5))
                    response = {
                        "header": "job",
                        "operation": self.math_primatives.add(),
                        "args": [random.randint(1, 10), random.randint(1, 10)],
                    }
=======
                    while len(self.jobs) == 0:
                        print("No jobs...")
                        time.sleep(1)

                    time.sleep(random.randint(1, 5))
                    response = self.pop_job().to_dict()
>>>>>>> origin/queuing

                elif data["header"] == "work_return":
                    print("Received result:", data["body"])
                    response = {"header": "message", "text": "Result received."}

                client_socket.sendall(pickle.dumps(response))

        client_socket.close()
        print("Disconnected from:", client_address)

    def stop(self):
        """Stops the server"""
        if self.server_socket:
            self.is_running = False
            self.server_socket.close()
            self.server_socket = None
            print("Server stopped.")

    def set_job(self, job: Job):
        print("Adding job:", job)
        self.jobs.append(job)

    def set_jobs(self, jobs: list):
        for job in jobs:
            try:
                self.set_job(job)
            except (
                Exception
            ) as exception:  # TODO: Add specific exception for if a Job is not passed
                print("An error occurred:", str(exception))
                self.stop()
                sys.exit(1)

    def pop_job(self):
        return self.jobs.pop()


if __name__ == "__main__":
    maths = MathPrimitives()
    server = JunkBoxServer("localhost", 8000)
    server.set_jobs(
        [
            Job(
                operation=maths.add(),
                args=[random.randint(1, 10), random.randint(1, 10)],
            ),
            Job(
                operation=maths.subtract(),
                args=[random.randint(1, 10), random.randint(1, 10)],
            ),
            Job(
                operation=maths.multiply(),
                args=[random.randint(1, 10), random.randint(1, 10)],
            ),
            Job(
                operation=maths.divide(),
                args=[random.randint(1, 10), random.randint(1, 10)],
            ),
        ]
    )
    server.start()


# To stop the server (you can call this from another part of your code)
# server.stop()
