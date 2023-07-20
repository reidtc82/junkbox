import socket


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
        message = "I\'m ready to do some work!"
        self.client_socket.sendall(message.encode("utf-8"))

        if inner_cmd.lower() == "quit":
            self.close()
            return

        # Receive the response from the server
        response = self.client_socket.recv(1024).decode("utf-8")
        print("Received response:", response)
        response = eval(response)
        return response

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
            'Enter a message to send \
                        to the server (or "quit" to exit): '
        )

        if command.lower() == "continue":
            job = client.request_work(command)
            print(job)
            for key, value in job.items():
                for _ in range(value):
                    print(key)


        if command.lower() == "quit":
            break
