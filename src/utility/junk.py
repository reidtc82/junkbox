import uuid


class Junk:
    """_summary_ : A class that represents a junk message."""

    header = None

    def __init__(self, header):
        self.header = header

    def to_dict(self):
        """_summary_ : Converts the junk message to a dictionary.

        Returns:
            _type_: _description_
        """
        return {"header": self.header}


class WorkRequest(Junk):
    """_summary_ : A class that represents a work request message.

    Args:
        Junk (_type_): _description_
    """

    body = None

    def __init__(self, body=None):
        self.body = body
        super().__init__("work_request")

    def to_dict(self):
        """_summary_ : Converts the work request message to a dictionary.

        Returns:
            _type_: _description_
        """
        return {"header": self.header, "body": self.body}


class WorkReturn(Junk):
    """_summary_ : A class that represents a work return message.
    Args:
        Junk (_type_): _description_
    """

    body = None

    def __init__(self, body=None):
        self.body = body
        super().__init__("work_return")

    def to_dict(self):
        """_summary_ : Converts the work return message to a dictionary.

        Returns:
            _type_: _description_
        """
        return {"header": self.header, "body": self.body}


class Job(Junk):
    """_summary_ : A class that represents a job message.

    Args:
        Junk (_type_): _description_
    """

    operation = None
    args = None
    id = None

    def __init__(self, operation=None, args=None):
        self.operation = operation
        self.args = args
        self.id = uuid.uuid4()
        super().__init__("job")

    def to_dict(self):
        """_summary_ : Converts the job message to a dictionary.

        Returns:
            _type_: _description_
        """
        return {"header": self.header, "operation": self.operation, "args": self.args}
