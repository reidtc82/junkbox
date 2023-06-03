import socket
import sys
import threading


class JunkBoxServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = None
        self.is_running = False

    def start(self):
        # Create a socket object
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            # Bind the socket to the server address and port
            self.server_socket.bind((self.host, self.port))

            # Listen for incoming connections
            self.server_socket.listen(5)
            print("Server is running and listening for connections...")
            self.is_running = True

            while self.is_running:
                # Wait for a client to connect
                client_socket, client_address = self.server_socket.accept()

                # Start a new thread to handle the client
                client_thread = threading.Thread(
                    target=self.handle_client, args=(client_socket, client_address)
                )
                client_thread.start()

        except KeyboardInterrupt:
            # Handling Keyboard Interrupt (Ctrl+C)
            print("Server shutdown initiated by keyboard interrupt...")
            self.stop()
            sys.exit(1)
        except Exception as e:
            # Handling other exceptions
            print("An error occurred:", str(e))
            self.stop()
            sys.exit(1)

    def handle_client(self, client_socket, client_address):
        print("Connected to:", client_address)

        while True:
            # Receive data from the client
            data = client_socket.recv(1024).decode("utf-8")
            print("Received data:", data)

            # If the client sends an empty message, disconnect
            if not data:
                break

            # Process the data (you can implement your own logic here)

            # Send a response back to the client
            if client_socket.fileno() != -1:
                response = "Hello from the server!"
                client_socket.sendall(response.encode("utf-8"))

        # Close the connection with the client
        client_socket.close()
        print("Disconnected from:", client_address)

    def stop(self):
        if self.server_socket:
            self.is_running = False
            self.server_socket.close()
            self.server_socket = None
            print("Server stopped.")


if __name__ == "__main__":
    # Usage example
    server = JunkBoxServer("localhost", 8000)
    server.start()

# To stop the server (you can call this from another part of your code)
# server.stop()
