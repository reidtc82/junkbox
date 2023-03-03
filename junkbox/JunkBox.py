# Import the necessary modules
from exceptions.LocationOutOfBoundsException import LocationOutOfBoundsException
# JunkBox class for use in junkbox
# A JunkBox is a matrix that can be used to perform matric math operations in the junkbox system
# This class will be used to create matrices that will be used in the junkbox
# data in the JunkBox must be numeric
class JunkBox:
    def __init__(self, rows: int, columns: int, data: list):
        self.rows = rows
        self.columns = columns
        self.data = data
    
    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def insert(self, row: int, column: int, data) -> None:
        # Insert data into the matrix at the specified row and column
        # check that the row and column are within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        # check that the data is numeric and raise TypeError if not
        if row > self.rows or column > self.columns:
            raise LocationOutOfBoundsException("The specified location is out of bounds")
        
        if not isinstance(data, (int, float)):
            raise TypeError("The data must be numeric")

        # insert the data into the matrix
        self.data[row][column] = data
    
    def get(self, row: int, column: int) -> object:
        # Get the data at the specified row and column
        # check that the row and column are within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows or column > self.columns:
            raise LocationOutOfBoundsException("The specified location is out of bounds")
        # return the data at the specified row and column
        return self.data[row][column]
    
    # function that returns specified row
    # returns a list
    # if the row is out of bounds, raise LocationOutOfBoundsException
    def get_row(self, row: int) -> list:
        # check that the row is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows:
            raise LocationOutOfBoundsException("The specified location is out of bounds")
        # return the row
        return self.data[row]
    
    def get_column(self, column: int) -> list:
        # check that the column is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if column > self.columns:
            raise LocationOutOfBoundsException("The specified location is out of bounds")
        # return the column
        return [row[column] for row in self.data]
    
    # function to remove entire row from JunkBox matrix
    # if the row is out of bounds, raise LocationOutOfBoundsException
    def remove_row(self, row: int) -> None:
        # check that the row is within the bounds of the matrix
        # if not, raise LocationOutOfBoundsException
        if row > self.rows:
            raise LocationOutOfBoundsException("The specified location is out of bounds")
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
            raise LocationOutOfBoundsException("The specified location is out of bounds")
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
        for i in range(len(column)):
            self.data[i].append(column[i])
        # increment the columns attribute
        self.columns += 1
        
    


