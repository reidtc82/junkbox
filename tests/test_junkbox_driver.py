import pytest
from src.junkbox_driver import JunkBoxPool, State
import time


# test that the junkboxpool class can be instantiated
def test_junkboxpool_instantiation():
    pool = JunkBoxPool()
    assert pool is not None


# test that the State class can be instantiated
def test_state_instantiation():
    state = State()
    assert state is not None


# test that JunkBoxPool can be used as a context manager
def test_junkboxpool_context_manager():
    with JunkBoxPool() as pool:
        assert pool is not None


# test JunkBoxPool apply_async method
# use multiprocessing Manager to share state between processes
# retrieve the result of the function call
# assert that the result is correct
def test_junkboxpool_apply_async():
    return_val = {}
    value = 1
    with JunkBoxPool() as pool:
        pool.apply_async(
            target=lambda x, y: y.update({x: x + 1}), args=(value, return_val)
        )
        assert return_val[value] == 2


# test JunkBoxPool map method creates processes
def test_junkboxpool_map():
    with JunkBoxPool() as pool:
        result = pool.map(lambda x: x + 1, [(1,), (2,), (3,)])
        time.sleep(1)
        assert len(result) == 3
        assert result[0].exitcode == 0
        assert result[1].exitcode == 0
        assert result[2].exitcode == 0


# test that map is using the JunkBoxPool processes and not making its own
def test_junkboxpool_map_processes():
    with JunkBoxPool() as pool:
        result = pool.map(lambda x: x + 1, [(1,), (2,), (3,)])
        assert result == pool.processes


# test JunkBoxPool join method pauses until all tasks are done
def test_junkboxpool_join():
    with JunkBoxPool() as pool:
        result = pool.map(lambda x: x + 1, (1,))
        pool.join()
        assert len(result) == 1
        for proc in result:
            assert proc.is_alive() is False
