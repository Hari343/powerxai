class Reading:
    # TODO: change this to represent whatever information is needed
    pass


# This is a fake database which stores data in-memory while the process is running
# Feel free to change the data structure to anything else you would like
database: dict[str, Reading] = {}


def add_reading(key: str, reading: Reading) -> None:
    """
    Store a reading in the database using the given key
    """
    database[key] = reading


def get_reading(key: str) -> Reading | None:
    """
    Retrieve a reading from the database using the given key
    """
    return database.get(key)
