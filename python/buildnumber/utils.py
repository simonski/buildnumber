import sys
import os


class IniFile(object):
    def __init__(self, filename=None):
        self.data = {}
        if filename is not None:
            self.filename = filename
            basename = filename.split("/")[-1]
            self.filename = filename
            self.root_dir = self.filename[0 : len(filename) - len(basename)]
            if os.path.isfile(filename):
                self.load()

    def load(self):
        f = open(self.filename, "r")
        for line in f:
            line = line.strip()
            whitespace = False
            comment = False
            header = False
            key = False
            if line == "":
                whitespace = True
            elif line.find("#") == 0:
                comment = True
            elif line.startswith("[") and line.endswith("]"):
                header = True
            elif line.find("=") > -1:
                key = True

            if whitespace or comment:
                continue
            elif header:
                # a new header
                current_header = {}
                header_key = line.strip("[]")
                if self.data.get(header_key) is None:
                    # saves against multiple declarations of the header
                    self.data[header_key] = {}
            elif key:
                key_name, value = line.split("=", 1)
                self.data[header_key][key_name] = value
        f.close()

    def save(self):
        f = open(self.filename, "w")
        for header_key in self.get_headers():
            line = "[" + header_key + "]"
            f.write(line)
            f.write("\n")
            for value_key in self.get_header_keys(header_key):
                line = value_key + "=" + self.get(header_key, value_key)
                f.write(line)
                f.write("\n")
            f.write("\n")
        f.close()

    def get(self, header, key, default_value=None):
        keys = self.data.get(header) or {}
        return keys.get(key) or default_value

    def set(self, header, key, value):
        keys = self.data.get(header) or {}
        self.data[header] = keys
        keys[key] = str(value)

    def get_headers(self):
        return self.data.keys()

    def get_header_keys(self, header):
        entry = self.data.get(header) or {}
        return entry.keys()

    def get_root_dir(self):
        return self.root_dir


class CLI:
    def __init__(self, argv=sys.argv):
        self.argv = argv

    def get_command(self):
        if len(self.argv) > 1:
            return self.argv[1]
        else:
            return None

    @staticmethod
    def read(prompt):
        return input(prompt)

    def index_of(self, key):
        index = 0
        while index < len(self.argv):
            if self.argv[index] == key:
                return index
            index += 1
        return -1

    def contains(self, key):
        return self.index_of(key) > -1

    def get_or_die(self, key, error_message=None):
        v = self.get_or_default(key, None)
        if v is None:
            if error_message is None:
                print("Error, '" + key + "' is required.")
            else:
                print(error_message)

            sys.exit(1)
        else:
            return v

    def get_or_default(self, key, default_value):
        index = self.index_of(key)
        if index == -1:
            return default_value
        else:
            if index + 1 < len(self.argv):
                return self.argv[index + 1]
            else:
                # means we have the key (e.g -f) but not hte value (e.g. -f filename)
                #  (missing filename)
                return default_value

    def get_existing_filename_or_die(self, key):
        """
        returns the filename specified by the key, or dies
        """
        filename = self.get_or_default(key, None)
        if filename is None:
            print("Error, '" + key + "' is required.")
            sys.exit(1)
        elif not os.path.isfile(filename):
            print("'" + str(filename) + "' is not a file.")
            sys.exit(1)
        else:
            return filename


def resolve_file(candidate):
    return candidate.replace("~", os.getenv("HOME"))


def split_file(candidate):
    """
    returns the directory path and the filename with no path information
    :param candidate:
    :return:
    """
    abs_file = resolve_file(candidate)
    filename = abs_file.split("/")[-1]
    index = len(filename) + 1
    dirname = abs_file[0:-index]
    return dirname, filename


class BuildnumberError(ValueError):
    def __init__(self, *args, **kwargs):  # real signature unknown
        pass
