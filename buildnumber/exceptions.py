import sys
import os


class BuildnumberError(ValueError):
    def __init__(self, *args, **kwargs):
        super(BlownumberError, self).__init__(args, kwargs)
