import os
import sys
import yaml

"""
A Buildfile looks like

name:1
    current:
    style: semantic / single_digit
    history:
        - 0_0_1: date
        - 0_0_2: date

name2:
    current: 0
    style: single_digit
    history:
        0: date
        1: date
        2: date
"""


class Buildfile:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load()

    def load(self):
        if os.path.isfile(self.filename):
            f = open(self.filename, "r")
            return yaml.load(f, Loader=yaml.FullLoader)
        else:
            return {}

    def save(self):
        f = open(self.filename, "w")
        f.write(yaml.dump(self.data, sort_keys=True))
        f.close()

    def get(self, name):
        info = self.data.get(name) or {}
        version = info.get("version") or "0"
        return str(version)

    def set(self, name, value):
        info = self.data.get(name) or {}
        self.data[name] = info
        info["version"] = value

    def increment(self, name):
        info = self.data.get(name) or {}
        self.data[name] = info
        version_type = info.get("type") or "integer"
        info["type"] = version_type

        old_version = info.get("version") or "0"
        if version_type == "semantic":
            new_version = old_version
        elif version_type == "integer":
            new_version = int(old_version) + 1

        info["version"] = new_version
