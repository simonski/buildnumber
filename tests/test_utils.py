import os
from buildnumber import model, bootstrap
from buildnumber import utils
from buildnumber.server import BuildnumberServer, BuildnumberServerConfig

DEFAULT_BUILDNUMBER_HOME="~/.buildnumber-testing"


def load_workflow_file(filename):
    w = model.Workflow()
    w.load_file(filename)
    return w


def load_workflow_yaml(yaml):
    w = model.Workflow()
    w.load_raw(yaml)
    return w


def create_server(root_dir=DEFAULT_BUILDNUMBER_HOME):
    # create a config that will be empty by default
    filename = utils.resolve_file(root_dir + "/buildnumber.cfg")
    db_filename = utils.resolve_file(root_dir + "/buildnumber.db")
    if os.path.isfile(db_filename):
        os.remove(db_filename)
    if os.path.isfile(filename):
        os.remove(filename)

    bootstrap.init(filename)

    config = BuildnumberServerConfig(filename)
    server = BuildnumberServer(config)
    return server

