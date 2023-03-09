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
    def dot_product(self):
        pass

    def cross_product(self, a, b):
        pass

    def transpose(self, a):
        pass

    def inverse(self, a):
        pass

    def determinant(self, a):
        pass

    def eigenvalues(self, a):
        pass

    def eigenvectors(self, a):
        pass

    def rank(self, a):
        pass

    def trace(self, a):
        pass

    def norm(self, a):
        pass

    def solve(self, a, b):
        pass

    def solve_linear(self, a, b):
        pass
