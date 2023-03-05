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


# test the JunkBox class getRow method
def test_JunkBox_get_row():
    # Test that the getRow method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Get the row at the specified row
    row = junkbox.get_row(0)
    # Test that the row was returned correctly
    assert row == [1, 2]


# test the JunkBox class get_column method
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


# test add_row method
def test_JunkBox_add_row():
    # Test that the add_row method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Add a row to the JunkBox matrix
    junkbox.add_row([5, 6])
    # Test that the row was added correctly
    assert junkbox.data == [[1, 2], [3, 4], [5, 6]]


# test add_column method
def test_JunkBox_add_column():
    # Test that the add_column method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Add a column to the JunkBox matrix
    junkbox.add_column([5, 6])
    # Test that the column was added correctly
    assert junkbox.data == [[1, 2, 5], [3, 4, 6]]


# test the merge function of the JunkBox class
# test axis 0
# create two JunkBox objects and merge them
def test_JunkBox_merge0():
    # Test that the merge method works correctly
    # Create a JunkBox object
    junkbox1 = JunkBox(2, 2, [[1, 2], [3, 4]])
    junkbox2 = JunkBox(2, 2, [[5, 6], [7, 8]])
    # Merge the two JunkBox objects
    junkbox3 = junkbox1.merge(junkbox2, 0)
    # Test that the merge was done correctly
    assert junkbox3.data == [[1, 2], [3, 4], [5, 6], [7, 8]]


# test axis 1
# create two JunkBox objects and merge them
def test_JunkBox_merge1():
    # Test that the merge method works correctly
    # Create a JunkBox object
    junkbox1 = JunkBox(2, 2, [[1, 2], [3, 4]])
    junkbox2 = JunkBox(2, 2, [[5, 6], [7, 8]])
    # Merge the two JunkBox objects
    junkbox3 = junkbox1.merge(junkbox2, 1)
    # Test that the merge was done correctly
    assert junkbox3.data == [[1, 2, 5, 6], [3, 4, 7, 8]]


# test the split function of the JunkBox class
# test axis 0
# create a JunkBox object and split it
def test_JunkBox_split0():
    # Test that the split method works correctly
    # Create a JunkBox object
    junkbox1 = JunkBox(4, 2, [[1, 2], [3, 4], [5, 6], [7, 8]])
    # Split the JunkBox object
    junkbox2, junkbox3 = junkbox1.split(axis=0, index=2)
    # Test that the split was done correctly
    assert junkbox2.data == [[1, 2], [3, 4]]
    assert junkbox3.data == [[5, 6], [7, 8]]


# test axis 1
# create a JunkBox object and split it
def test_JunkBox_split1():
    # Test that the split method works correctly
    # Create a JunkBox object
    junkbox1 = JunkBox(2, 4, [[1, 2, 5, 6], [3, 4, 7, 8]])
    # Split the JunkBox object
    junkbox2, junkbox3 = junkbox1.split(axis=1, index=2)
    # Test that the split was done correctly
    assert junkbox2.data == [[1, 2], [3, 4]]
    assert junkbox3.data == [[5, 6], [7, 8]]


# test the T property of the JunkBox class
# create a JunkBox object and transpose it
def test_JunkBox_T():
    # Test that the T property works correctly
    # Create a JunkBox object
    junkbox1 = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Transpose the JunkBox object
    junkbox2 = junkbox1.T
    # Test that the transpose was done correctly
    assert junkbox2.data == [[1, 3], [2, 4]]


# test JunkBox class __str__ method
def test_JunkBox_str():
    # Test that the __str__ method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Test that the __str__ method works correctly
    assert str(junkbox) == "[[1, 2], [3, 4]]"


# test junkbox class __repr__ method
def test_JunkBox_repr():
    # Test that the __repr__ method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Test that the __repr__ method works correctly
    assert repr(junkbox) == "[[1, 2], [3, 4]]"


# test junkbox prperty shape
def test_JunkBox_shape():
    # Test that the shape property works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Test that the shape property works correctly
    assert junkbox.shape == (2, 2)


# test JunkBox insert_row method
def test_JunkBox_insert_row():
    # Test that the insert_row method works correctly
    # Create a JunkBox object
    junkbox = JunkBox(2, 2, [[1, 2], [3, 4]])
    # Insert a row into the JunkBox matrix
    junkbox.insert_row(row=[5, 6], index=1)
    # Test that the row was inserted correctly
    assert junkbox.data == [[1, 2], [5, 6], [3, 4]]
