import socket
import sys
import dill as pickle


class MySocketClient:
    def __init__(self, server_address):
        self.server_address = server_address
        self.client_socket = None

    def connect(self):
        # Create a socket object
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to the server
        self.client_socket.connect(self.server_address)
        print("Connected to the server:", self.server_address)

    def request_work(self, inner_cmd) -> dict():
        # Send a message to the server
        message = {"header": "work_request", "body": {}}
        self.client_socket.sendall(pickle.dumps(message))

        if inner_cmd.lower() == "quit":
            self.close()
            return

        # Receive the response from the server
        response = pickle.loads(self.client_socket.recv(1024))
        # print("Received response:", response)
        # response = eval(response)
        return response

    def return_work(self, res):
        # Send a message to the server
        message = {"header": "work_return", "body": res}
        self.client_socket.sendall(pickle.dumps(message))

        # Receive the response from the server
        response = pickle.loads(self.client_socket.recv(1024))
        print("Received response:", response)

    def close(self):
        if self.client_socket:
            # Close the connection with the server
            self.client_socket.close()
            self.client_socket = None
            print("Connection closed.")


if __name__ == "__main__":
    # Usage example
    client = MySocketClient(("localhost", 8000))
    client.connect()

    while True:
        command = input(
            "Enter start to begin requesting work \n"
            + 'from the server (or "quit" to exit): '
        )

        if command.lower() == "start":
            while True:
                try:
                    job = client.request_work(command)
                    result = job["operation"](*job["args"])
                    print(
                        "Executing "
                        + job["operation"].__name__
                        + " on "
                        + str(job["args"])
                        + "\t\t",
                        result,
                    )
                    client.return_work(result)
                except KeyboardInterrupt:
                    print("Client shutdown initiated by keyboard interrupt...")
                    client.close()
                    sys.exit(1)

        if command.lower() == "quit":
            client.close()
            sys.exit(0)
