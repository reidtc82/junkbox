class Junk:
    """_summary_ : A class that represents a junk message."""

    header = None

    def __init__(self, header):
        self.header = header


class WorkRequest(Junk):
    """_summary_ : A class that represents a work request message.

    Args:
        Junk (_type_): _description_
    """

    body = None

    def __init__(self, body=None):
        self.body = body
        super().__init__("work_request")


class WorkReturn(Junk):
    """_summary_ : A class that represents a work return message.
    Args:
        Junk (_type_): _description_
    """

    body = None

    def __init__(self, body=None):
        self.body = body
        super().__init__("work_return")


class Job(Junk):
    """_summary_ : A class that represents a job message.

    Args:
        Junk (_type_): _description_
    """

    operation = None
    args = None

    def __init__(self, operation=None, args=None):
        self.operation = operation
        self.args = args
        super().__init__("job")
