# This is the broker for junkbox
# When launched it runs until it is killed
# It manages a list of all connected executors by exposing a socket server where executors can register themselves
# It maintains a queue of work to be sent to the executors
# It will send work to executors when they are available
# It will monitor executors through a heartbeat
# It will remove executors from teh executor registry that have not sent a heartbeat in a while

# imports
import socket
import threading
import time
import selectors
import types


class Broker:
    # class to represent the broker
    status = "paused"
    executors = {}
    REGISTRY_HOST = "127.0.0.1"
    REGISTRY_PORT = 5000

    def __init__(self) -> None:
        self.sel = selectors.DefaultSelector()

        self.thread_pool = []
        self.thread_pool.append(threading.Thread(target=self.shell))
        self.thread_pool.append(threading.Thread(target=self.heartbeat_monitor))
        self.thread_pool.append(
            threading.Thread(target=self.registry_server, args=(self.executors,))
        )
        for thread in self.thread_pool:
            thread.start()
        # wait for the threads to finish
        for thread in self.thread_pool:
            thread.join()

        # create a shared object called executors to store the executors that is accessible from all the threads
        # this is a dictionary of executors
        # the key is the executor id
        # the value is the metadata of the executor:
        #   - ip address
        #   - port
        #   - last heartbeat
        #   - status
        #   - number of jobs completed
        #   - number of jobs failed
        #   - number of jobs running
        #   - number of jobs pending
        #   - number of jobs queued
        #   - number of jobs total

    def _accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def _service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.outb += recv_data
            else:
                print(f"Closing connection to {data.addr}")
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print(f"Echoing {data.outb!r} to {data.addr}")
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    # function to present the shell for administration
    def shell(self) -> None:
        # present a shell to the user
        # allow the user to administer the broker
        # wait for input and process the commands entered
        # commands:
        #   - --executors, --E : list executors
        #   - --pending, --P : list pending jobs
        #   - --jobs, --J : list active jobs
        #   - --help, --H : list commands (list all commands that can be run)
        #   - --start : start broker
        #   - --stop: stop broker
        #   - --resume : resume broker
        #   - --exit : exit

        # when the broker is initialized it will be in a paused state
        # the broker will not send work to executors until it is started
        # the broker will not accept new executors until it is started
        # the broker will not accept new jobs until it is started
        # the broker will not remove executors from the registry until it is started
        # the broker will not remove jobs from the registry until it is started

        # when the broker is paused it will still accept commands from the shell
        # the broker will not send work to executors until it is resumed
        # the broker will not accept new executors until it is resumed
        # the broker will not accept new jobs until it is resumed
        # the broker will not remove executors from the registry until it is resumed
        # the broker will not remove jobs from the registry until it is resumed

        # clear the screen and hide the cursor
        # print the welcome message

        print("Welcome to the junkbox broker shell")
        print("Type --help or --H to see a list of commands")
        print("Type --exit to exit the shell")
        print("Current status: " + self.status)
        # create a loop to accept commands
        while True:
            # print the prompt
            # get the input from the user
            # process the input from the user
            print("junkbox> ", end="")
            command = input()
            # if the command is --exit then exit the shell
            # TODO: Refactor this to a dictionary one day
            if command == "--exit":
                print("Exiting shell")
                # broadcast the exit command to the threads
                self.status = "exiting"
                break
            # if the command is --help then print the help message
            elif command == "--help" or command == "--H":
                print("Commands:")
                print("\t--executors, --E : list executors")
                print("\t--pending, --P : list pending jobs")
                print("\t--jobs, --J : list active jobs")
                print(
                    "\t--help, --H : list commands (list all commands that can be run)"
                )
                print("\t--start : start broker")
                print("\t--stop: stop broker")
                print("\t--resume : resume broker")
                print("\t--exit : exit")
            # if the command is --executors then list the executors
            elif command == "--executors" or command == "--E":
                self.list_executors()
            # if the command is --pending then list the pending jobs
            elif command == "--pending" or command == "--P":
                print("Listing pending jobs")
            # if the command is --jobs then list the active jobs
            elif command == "--jobs" or command == "--J":
                print("Listing active jobs")
            # if the command is --start then start the broker
            elif command == "--start":
                self.status = "running"
                print("Starting broker")
            # if the command is --stop then stop the broker
            elif command == "--stop":
                self.status = "stopped"
                print("Stopping broker")
            # if the command is --resume then resume the broker
            elif command == "--resume":
                self.status = "running"
                print("Resuming broker")
            # if the command is not recognized then print an error message
            else:
                print("Command not recognized")

    def heartbeat_monitor(self) -> None:
        # monitor the heartbeat of the executors
        # remove executors from the registry that have not sent a heartbeat in a while
        did_print = False
        while True:
            # check for exit broadcast from the shell thread
            # if the exit broadcast is received then exit the thread
            if self.status == "exiting":
                print("Exiting heartbeat monitor")
                break
            if self.status == "stopped":
                # print "Heartbeat monitor stopped" once and then pass
                if did_print is False:
                    print("Heartbeat monitor stopped")
                    did_print = True
            else:
                if did_print is True:
                    did_print = False
                print("bump bump")
                # TODO: check the heartbeat of the executors
                # sleep for 5 seconds
                time.sleep(5)

    def registry_server(self, executors) -> None:
        # listen on a port set in the configuration file for new executors to register through
        # when a new executor registers add it to the executor registry

        did_print = False
        did_init = False
        # check for exit broadcast from the shell thread
        # if the exit broadcast is received then exit the thread
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # conn, addr = s.accept()

        # with conn:
        #     print("Connected by", addr)
        #     # add the new executor into the registry dict
        #     executors[uuid.uuid4().hex] = {"address": addr}
        #     while True:
        #         data = conn.recv(1024)
        #         if not data:
        #             break
        #         conn.sendall(data)
        try:
            print("Am I here?")
            while self.status == "running":
                if not did_init:
                    did_init = True
                    print("Starting registry server")
                    sock.bind((self.REGISTRY_HOST, self.REGISTRY_PORT))
                    sock.listen()

                    print(f"Listening on {(self.REGISTRY_HOST, self.REGISTRY_PORT)}")
                    sock.setblocking(False)
                    self.sel.register(sock, selectors.EVENT_READ, data=None)

                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self._accept_wrapper(key.fileobj)
                    else:
                        self._service_connection(key, mask)

            if self.status == "exiting":
                self.sel.close()
                print("Exiting registry server")
            if self.status == "stopped":
                # print "Heartbeat monitor stopped" once and then pass
                self.sel.close()
                did_init = False
                if did_print is False:
                    print("Registry server stopped")
                    did_print = True
        except KeyboardInterrupt:
            print("Caught keyboard interrupt, exiting")

    # function that lists a pretty formatted list of executors
    def list_executors(self) -> None:
        print("Listing executors")
        for executor in self.executors:
            print(executor)
        print("Done listing executors")


if __name__ == "__main__":
    # initialize the broker in a paused state
    # present a lightweight shell to the user
    # allow the user to administer the broker
    broker = Broker()
