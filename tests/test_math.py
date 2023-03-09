# pytest file to test the math and mathprimatives classes
# test that the mathprimatives class can be instantiated
# test that the mathprimatives class can return a function
# test that the mathprimatives class can return a function that adds two numbers
# test that the mathprimatives class can return a function that subtracts two numbers
# test that the mathprimatives class can return a function that multiplies two numbers
# test that the mathprimatives class can return a function that divides two numbers
# test that the math class can be instantiated

import pytest
from junkbox.math import MathPrimitives, Math


# test that the mathprimatives class can be instantiated
def test_mathprimatives_instantiation():
    mathprimatives = MathPrimitives()
    assert mathprimatives is not None


# test that the mathprimatives class can return a function
def test_mathprimatives_return_function():
    mathprimatives = MathPrimitives()
    assert mathprimatives.add() is not None


# test that the mathprimatives class can return a function that adds two numbers
def test_mathprimatives_add():
    mathprimatives = MathPrimitives()
    assert mathprimatives.add()(1, 2) == 3


# test that the mathprimatives class can return a function that subtracts two numbers
def test_mathprimatives_subtract():
    mathprimatives = MathPrimitives()
    assert mathprimatives.subtract()(1, 2) == -1


# test that the mathprimatives class can return a function that multiplies two numbers
def test_mathprimatives_multiply():
    mathprimatives = MathPrimitives()
    assert mathprimatives.multiply()(1, 2) == 2


# test that the mathprimatives class can return a function that divides two numbers
def test_mathprimatives_divide():
    mathprimatives = MathPrimitives()
    assert mathprimatives.divide()(1, 2) == 0.5


# test that the math class can be instantiated
def test_math_instantiation():
    math = Math(None)
    assert math is not None
