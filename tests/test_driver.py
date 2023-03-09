import pytest
from junkbox.driver import Driver

# series of tests to test driver functions
# test that the driver can be instantiated
# test that the driver can start the socket listener
# test that the driver can stop the socket listener
# test that the driver can pause the socket listener
# test that the driver can add an executor to the executor list


def test_driver_instantiation():
    driver = Driver("1.1.1.1", 1234, 1000)
    assert driver is not None


# test driver properties
def test_driver_properties():
    driver = Driver("1.1.1.1", 1234, 1000)
    assert driver.ip_address == "1.1.1.1"
    assert driver.listener_port == 1234
    assert driver.port_range == 1000

