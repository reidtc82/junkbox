# Import the necessary modules
from __future__ import annotations

from exceptions.jb_errors import LocationOutOfBoundsException, RowLengthException


# JunkBox class for use in junkbox
# A JunkBox is a matrix that can be used to perform matric math operations in
# the junkbox system
# This class will be used to create matrices that will be used in the junkbox
# data in the JunkBox must be numeric
class JunkBox:
    """
    A JunkBox is a matrix that can be used to perform matric math operations
    in the junkbox system
    This class will be used to create matrices that will be used in the junkbox
    data in the JunkBox must be numeric

    Attributes:
        rows (int): The number of rows in the matrix
        columns (int): The number of columns in the matrix
        data (list): The data in the matrix

    Methods:
        __init__(self, rows: int, columns: int, data: list): The constructor
                                for the JunkBox class
        __str__(self): The string representation of the JunkBox class
        __repr__(self): The string representation of the JunkBox class
        insert(self,row: int, column: int, data) -> None: Insert data into the
        matrix at the specified row and column
        get(self, row: int, column: int) -> object: Get the data at the
        specified row and column
        get_row(self, row: int) -> list: Get the specified row
        get_column(self, column: int) -> list: Get the specified column
        remove_row(self, row: int) -> None: Remove the specified row
        remove_column(self, column: int) -> None: Remove the specified column
        add_row(self, row: list) -> None: Add the specified row
        add_column(self, column: list) -> None: Add the specified column
        merge(self, other: JunkBox, axis: int) -> None: Merge this JunkBox
                    with another JunkBox
    """

    def __init__(self, rows: int, columns: int, data: list):
        self.rows = rows
        self.columns = columns
        self.data = data

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    # function to transpose the JunkBox matrix
    # can be called by JunkBox.T
    # T is a property of the JunkBox class
    @property
    def T(self) -> JunkBox:
        # create a new JunkBox object with the rows and columns swapped
        # return the new JunkBox object
        return JunkBox(self.columns, self.rows, self.get_columns())

    # property shape of JunkBox class
    # returns a tuple of the rows and columns
    @property
    def shape(self) -> tuple:
        return self.rows, self.columns

    def insert(self, row: int, column: int, data) -> None:
        # Insert data into the matrix at the specified row and column
        # check that the row and column are within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        # check that the data is numeric and raise TypeError if not
        if row > self.rows or column > self.columns:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )

        if not isinstance(data, (int, float)):
            raise TypeError("The data must be numeric")

        # insert the data into the matrix
        self.data[row][column] = data

    def get(self, row: int, column: int) -> object:
        # Get the data at the specified row and column
        # check that the row and column are within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows or column > self.columns:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # return the data at the specified row and column
        return self.data[row][column]

    # function that returns specified row
    # returns a list
    # if the row is out of bounds, raise LocationOutOfBoundsException
    def get_row(self, row: int) -> list:
        # check that the row is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # return the row
        return self.data[row]

    def get_rows(self) -> list:
        # return a list of the rows in data
        return self.data

    def get_columns(self) -> list:
        # return a list of the columns in data
        return [self.get_column(i) for i in range(self.columns)]

    def get_column(self, column: int) -> list:
        # check that the column is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if column > self.columns:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # return the column
        return [row[column] for row in self.data]

    # function to remove entire row from JunkBox matrix
    # if the row is out of bounds, raise LocationOutOfBoundsException
    def remove_row(self, row: int) -> None:
        # check that the row is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # remove the row
        self.data.pop(row)
        # decrement the rows attribute
        self.rows -= 1

    # function to remove entire column from JunkBox matrix
    # if the column is out of bounds, raise LocationOutOfBoundsException
    def remove_column(self, column: int) -> None:
        # check that the column is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if column > self.columns:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # remove the column
        for row in self.data:
            row.pop(column)
        # decrement the columns attribute
        self.columns -= 1

    def add_row(self, row: list) -> None:
        # check that the row is the correct length
        # if not, raise ValueError
        if len(row) != self.columns:
            raise ValueError("The row must be the correct length")
        # add the row to the matrix
        self.data.append(row)
        # increment the rows attribute
        self.rows += 1

    def add_column(self, column: list) -> None:
        # check that the column is the correct length
        # if not, raise ValueError
        if len(column) != self.rows:
            raise ValueError("The column must be the correct length")
        # add the column to the matrix
        # enumerate through the columns instead of range(len())
        # enumerate column and append column[i] to self.data[i]
        for i, val in enumerate(column):
            self.data[i].append(val)
        # increment the columns attribute
        self.columns += 1

    def merge(self, other: JunkBox, axis: int) -> None:
        # check that the axis is 0 or 1
        # if not, raise ValueError
        if axis not in (0, 1):
            raise ValueError("The axis must be 0 or 1")
        # check that the other JunkBox is the same size as this JunkBox
        # if not, raise ValueError
        if axis == 0 and other.columns != self.columns:
            raise ValueError("The JunkBoxes must have the same number of columns")
        if axis == 1 and other.rows != self.rows:
            raise ValueError("The JunkBoxes must have the same number of rows")
        # merge the JunkBoxe
        if axis == 0:
            for row in other.data:
                self.add_row(row)
        if axis == 1:
            # loop through the columns of other and add them to this JunkBox
            # use the add_column function
            for column in other.get_columns():
                self.add_column(column)

        return self

    def split(self, axis: int, index: int) -> tuple:
        # check that the axis is 0 or 1
        # if not, raise ValueError
        if axis not in (0, 1):
            raise ValueError("The axis must be 0 or 1")
        # check that the index is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if axis == 0 and index > self.rows:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        if axis == 1 and index > self.columns:
            raise LocationOutOfBoundsException(
                "The specified location is out of bounds"
            )
        # split the JunkBox
        # create two new JunkBox objects
        # if axis is 0, split at the row
        # if axis is 1, split at the column
        if axis == 0:
            # create a new JunkBox object with the rows above the index
            # create a new JunkBox object with the rows below the index
            # return the two JunkBox objects
            return JunkBox(index, self.columns, self.data[:index]), JunkBox(
                self.rows - index, self.columns, self.data[index:]
            )
        if axis == 1:
            # create a new JunkBox object with the columns to the left of the index
            # create a new JunkBox object with the columns to the right of the index
            # return the two JunkBox objects
            return (
                JunkBox(self.rows, index, [row[:index] for row in self.data]),
                JunkBox(
                    self.rows, self.columns - index, [row[index:] for row in self.data]
                ),
            )

        return None

    # function to insert a row into JunkBox matrix
    # if the row is longer than the number of columns, raise RowLengthException
    # function must use the split, merge, and add_row functions
    def insert_row(self, row: list, index: int) -> None:
        # check that the row is the correct length
        # if not, raise ValueError
        if len(row) != self.columns:
            raise RowLengthException("The row must be the correct length")
        # split the JunkBox at the index
        # merge the JunkBox with the new row
        # merge the JunkBox with the other JunkBox
        # use the split, merge, and add_row functions
        junkbox1, junkbox2 = self.split(0, index)
        junkbox1.add_row(row)
        junkbox1.merge(junkbox2, 0)
        self.data = junkbox1.data
        self.rows += 1
