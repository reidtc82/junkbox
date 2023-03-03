# This is the LocationOutOfBoundsException for junkbox
# It is raised when a user attempts to place data in a location outside the bounds of the matrix
class LocationOutOfBoundsException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message

    def __repr__(self):
        return self.message
