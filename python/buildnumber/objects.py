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

DEFAULT_NAME = "default"
DEFAULT_TYPE = "semantic"


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

    def init(self, name, init_type):
        info = {}
        info["type"] = init_type
        self.data[name] = info
        info["version"] = self.get(name)

    def save(self):
        f = open(self.filename, "w")
        f.write(yaml.dump(self.data, sort_keys=True))
        f.close()

    def get(self, name=DEFAULT_NAME):
        info = self.data.get(name) or {}
        version_type = info.get("type") or DEFAULT_TYPE
        if version_type == "integer":
            default_version = "0"
        else:
            default_version = "0.0.0"

        version = info.get("version") or default_version
        return str(version)

    def set(self, name, value):
        info = self.data.get(name) or {}
        self.data[name] = info
        info["version"] = value

    def split_semantic_version(self, version):
        splits = version.split(".")
        return splits[0], splits[1], splits[2]

    def increment(self, name, increment_type="revision"):
        info = self.data.get(name) or {}
        self.data[name] = info
        version_type = info.get("type") or DEFAULT_TYPE
        info["type"] = version_type

        if version_type == "semantic":
            old_version = info.get("version") or "0.0.0"
            major, minor, revision = self.split_semantic_version(old_version)
            if increment_type == "revision":
                revision = str(int(revision) + 1)
            elif increment_type == "minor":
                minor = str(int(minor) + 1)
                revision = "0"
            elif increment_type == "major":
                major = str(int(major) + 1)
                minor = "0"
                revision = "0"
            new_version = major + "." + minor + "." + revision

        elif version_type == "integer":
            old_version = info.get("version") or "0"
            new_version = int(old_version) + 1

        info["version"] = new_version
