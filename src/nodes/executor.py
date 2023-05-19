# executor class that connects to the broker through the registery server
# and sends heartbeats to the heartbeat monitor
# and also receives the tasks from the broker and executes them
# and sends the results back to the broker

# for mvp this simply needs to connect to the registry server and send heartbeats
# when it makes a connection to the broker it should send a message to the registry server
# to let it know that it is connected to the broker
# that message should contain the executors ip and port

import socket


class Executor:
    def __init__(self):
        print("Executor created")
        self.broker_registry_port = 5000
        self.broker_registry_ip = "127.0.0.1"

        self.connect_to_registry()

    def connect_to_registry(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.broker_registry_ip, self.broker_registry_port))
            s.sendall(b"Hello, world")
            data = s.recv(1024)

        print(f"Received {data!r}")


if __name__ == "__main__":
    executor = Executor()
