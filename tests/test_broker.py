# file to test the broker node 
# This should use the broker.py file to test the broker node
# this should use pytest to test the broker node

import pytest

from junk_box.src.nodes import Broker


def test_broker():
    # test the broker node
    # create a broker node
    broker = Broker()
    # test the broker node
    assert broker is not None

# test that the broker node can be started
def test_broker_start():
    # create a broker node
    broker = Broker()
    # start the broker node
    broker.start()
    # determine if the broker node is running
    assert broker.is_running == True

# test that the broker node can be stopped
def test_broker_stop():
    # create a broker node
    broker = Broker()
    # start the broker node
    broker.start()
    # stop the broker node
    broker.stop()
    # determine if the broker node is running
    assert broker.is_running == False