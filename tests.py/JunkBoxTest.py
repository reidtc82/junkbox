# These are pytest tests for JunkBox class
# These tests are used to test the JunkBox class

import pytest
from JunkBox import JunkBox

# Test the JunkBox class
# Test the JunkBox class constructor
def test_JunkBox_constructor():
    # Test that the constructor works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Test that the rows attribute is set correctly
    assert junkbox.rows == 2
    # Test that the columns attribute is set correctly
    assert junkbox.columns == 2
    # Test that the data attribute is set correctly
    assert junkbox.data == [[1, 2], [3, 4]]

# Test the JunkBox class insert method
def test_JunkBox_insert():
    # Test that the insert method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Insert data into the matrix
    junkbox.insert(0, 0, 5)
    # Test that the data was inserted correctly
    assert junkbox.data == [[5, 2], [3, 4]]

# Test the JunkBox class get method
def test_JunkBox_get():
    # Test that the get method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Get the data at the specified row and column
    data = junkbox.get(0, 0)
    # Test that the data was returned correctly
    assert data == 1

#test the JunkBox class getRow method
def test_JunkBox_getRow():
    # Test that the getRow method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Get the row at the specified row
    row = junkbox.getRow(0)
    # Test that the row was returned correctly
    assert row == [1, 2]