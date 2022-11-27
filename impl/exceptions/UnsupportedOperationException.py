from typing import Union

class UnsupportedOperationException(Exception):
    def __init__(self, msg: Union[str, None] = None):
        if msg is None:
            msg = 'Attempted to perform an unsupported operation'

        super().__init__(msg)
