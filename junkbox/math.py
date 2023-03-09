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

    def add(self, a, b):
        # split a and b JunkBox objects into granular list of cells
        # pass the cells to the driver with the add function to be queued for execution
        # the driver will create jobs and send them to the executors
        # the driver will then wait for the results and return them to the user
        pass
