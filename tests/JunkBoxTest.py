# These are pytest tests for JunkBox class
# These tests are used to test the JunkBox class

import pytest
from junkbox.JunkBox import JunkBox

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
def test_JunkBox_get_row():
    # Test that the getRow method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Get the row at the specified row
    row = junkbox.get_row(0)
    # Test that the row was returned correctly
    assert row == [1, 2]


#test the JunkBox class get_column method
def test_JunkBox_get_column():
    # Test that the get_column method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Get the column at the specified column
    column = junkbox.get_column(0)
    # Test that the column was returned correctly
    assert column == [1, 3]

# test remove_row method
def test_JunkBox_remove_row():
    # Test that the remove_row method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Remove the row at the specified row
    junkbox.remove_row(0)
    # Test that the row was removed correctly
    assert junkbox.data == [[3, 4]]

# test remove_column method
def test_JunkBox_remove_column():
    # Test that the remove_column method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Remove the column at the specified column
    junkbox.remove_column(0)
    # Test that the column was removed correctly
    assert junkbox.data == [[2], [4]]

#test add_row method
def test_JunkBox_add_row():
    # Test that the add_row method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Add a row to the JunkBox matrix
    junkbox.add_row([5, 6])
    # Test that the row was added correctly
    assert junkbox.data == [[1, 2], [3, 4], [5, 6]]

#test add_column method
def test_JunkBox_add_column():
    # Test that the add_column method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Add a column to the JunkBox matrix
    junkbox.add_column([5, 6])
    # Test that the column was added correctly
    assert junkbox.data == [[1, 2, 5], [3, 4, 6]]