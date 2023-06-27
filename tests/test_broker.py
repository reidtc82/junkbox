# file to test the broker node
# This should use the broker.py file to test the broker node
# this should use pytest to test the broker node

import socket

from junkbox.src.nodes.broker import JunkBoxServer

SERVER_IP = "localhost"
SERVER_PORT = 8000


def test_broker():
    """Test the broker node can be created"""

    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)

    assert broker is not None
    assert broker.host == SERVER_IP
    assert broker.port == SERVER_PORT


def test_broker_start():
    """Test that the broker node can be started"""

    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()

    assert broker.is_running is True


def test_broker_stop():
    """Test that the broker node can be stopped"""

    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()
    broker.stop()

    assert broker.is_running is False


def test_broker_restart():
    """Test that the broker node can be restarted"""
    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()
    broker.stop()
    broker.start()

    assert broker.is_running is True


def test_broker_socket():
    """Test that the broker node has a socket object"""
    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()

    assert broker.server_socket is not None


def test_broker_socket_close():
    """Test that the broker closes the socket when stopped"""
    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()
    broker.stop()

    assert broker.server_socket is None


def test_broker_socket_restart():
    """Test that the broker restarts the socket when restarted"""
    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()
    broker.stop()
    broker.start()

    assert broker.server_socket is not None


def test_socket_connect():
    """Test that the broker can accept a connection"""
    broker = JunkBoxServer(SERVER_IP, SERVER_PORT)
    broker.start()

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_IP, SERVER_PORT))

    assert client_socket is not None
