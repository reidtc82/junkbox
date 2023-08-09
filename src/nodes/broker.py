import random
import socket
import sys
import threading
import time
import dill as pickle
from src.utility.math import MathPrimitives

# def add(a, b):
#     return a + b


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

    def start(self):
        """Starts the server"""
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
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

            if client_socket.fileno() != -1: # -1 means an error occurred
                if data['header'] == "work_request":
                    time.sleep(random.randint(1, 5))
                    response = {
                        "operation": self.math_primatives.add(),
                        "args": [random.randint(1, 10), random.randint(1, 10)],
                    }
                    
                elif data['header'] == "work_return":
                    print("Received result:", data["body"])
                    response = {"Result received."}

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


if __name__ == "__main__":
    server = JunkBoxServer("localhost", 8000)
    server.start()

# To stop the server (you can call this from another part of your code)
# server.stop()
