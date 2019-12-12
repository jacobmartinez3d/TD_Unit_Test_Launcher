import re
import importlib
import json
import sys
import os
import unittest
from pprint import pprint, pformat

CONFIG_PATH = "config.json"

__version__ = 0.2


def load_config(config_path=None):
    """load each line in config.txt into dictionary.

    :param config_path: <str> Path to config txt
    """
    config_dict = {}
    with open(config_path or CONFIG_PATH, "r") as config:

        config_dict = json.load(config)

    return config_dict


def _get_py_files(location):
    """Scan the location directory and return a list of .py filenames.
    scandir is reccomended for speed and handling of overlength Windows paths.

    :param location: <str> location to scan in.
    """
    py_files = []

    try:
        location = os.scandir(location)

    except OSError:
        print("The path:\n\t'{}'\ndoes not exist!\n".format(location))
        location = []

    for dir_entry in location:
        if dir_entry.is_file() and re.search(r"\.py$", dir_entry.name.lower()):
            py_files.append(dir_entry.name)

    return py_files


def run(config):
    """Import each python file detected in TESTS_LOCATION.

    :param config: containing info from config.txt.
    :type  config: dict
    """
    tests_location = config["tests_location"]
    test_results = None

    sys.path.append(tests_location)

    for py_file_entry in _get_py_files(tests_location):

        py_file_module_path = os.path.splitext(py_file_entry)[0]
        # import file as module
        test_module = importlib.import_module(
            py_file_module_path.replace("\\", "/"))

        # unittest suite
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(
            test_module.TestMain)
        # test_results is a unittest.TestResult object
        test_results = unittest.TextTestRunner().run(suite)

        # print(test_results.errors)
        # print(test_results.failures)

    sys.path.remove(tests_location)

    return test_results


# load config from config.txt
CONFIG_DICT = load_config()
# run unit test launcher
sys.stdout.write(run(CONFIG_DICT))

# uncomment below line to automatically quit Touch Designer after running tests.
# exit()
