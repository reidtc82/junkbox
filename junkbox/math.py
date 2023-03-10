# class that produces mathematical functions
# these functions can only operate on JunkBox objects
# and return JunkBox objects
# The functions must be returned so that the driver can pass them to the executors
# The driver will then wait for the results and return them to the user.
#
# The driver will expose an api to the user that will allow
# the user to perform matix math operations
# The user will create matrices and then perform operations on them.
# The driver will then create jobs
# and send them to the executors.
# The driver will then wait for the results and return them to the user.
# this class should act like a factory for mathematical functions
# the functions should be returned so that the driver can pass them to the executors


from junkbox.JunkBox import JunkBox
import uuid


class MathPrimitives:
    def __init__(self):
        pass

    def add(self) -> callable:
        return lambda a, b: a + b

    def subtract(self):
        return lambda a, b: a - b

    def multiply(self):
        return lambda a, b: a * b

    def divide(self):
        return lambda a, b: a / b


class Math:
    # has a junkbox-driver object as a member
    def __init__(self, driver):
        self.driver = driver
        self.primitives = MathPrimitives()

    def add(self, a: JunkBox, b: JunkBox) -> JunkBox:
        # split a and b JunkBox objects into granular list of cells
        # pass the cells to the driver with the add function to be queued for execution
        # the driver will create jobs and send them to the executors
        # the driver will then wait for the results and return them to the user
        # get the number of executors from driver
        # get the number of cells from a and b
        # divide the number of cells by the number of executors
        # round up to the nearest integer
        # this will be the number of cells to be sent to each executor
        # create a list of cells to be sent to each executor

        ex_count = len(self.driver.executors)
        a_rows, a_cols = a.shape
        b_rows, b_cols = b.shape

        # using recursion split() the JunkBox objects into segments
        # these should be based on the number of executors available

        # a1, a2 = a.split(0, a_row_part)

        # a1_1, a1_2 = a1.split(1, a_col_part)

        # self.driver.job_queue.append(
        #     {
        #         "jb_1": a1_1,
        #         "jb_2": b1_1,
        #         "function": self.primitives.add(),
        #         "uuid": uuid.uuid4(),
        #     }
        # )
