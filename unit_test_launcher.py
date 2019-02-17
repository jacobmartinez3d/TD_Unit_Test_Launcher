import re
import importlib
import sys
import os
from pprint import pformat

CONFIG_PATH = "config.txt"

__version__ = 0.1


def load_config(config_path=CONFIG_PATH):
    """load each line in config.txt into dictionary.

    :param config_path: <str> Path to config txt
    """
    config_dict = {}
    with open(config_path, "r") as config:

        content = [line.strip().split(" ")
                   for line in config.readlines()]
        content = list(filter(lambda x: len(x) == 2, content))
        [config_dict.update({line[0]:line[1]}) for line in content]

    return config_dict


def _get_py_files(location):
    """Scan the location directory and return a list of .py filenames.
    scandir is reccomended for speed and handling of overlength Windows paths.
    """
    py_files = []

    try:
        location = os.scandir(location)

    except OSError:
        print("The path:\n\t'{}'\ndoes not exist!\n".format(location))

    for dir_entry in location:
        if dir_entry.is_file() and re.search(r"\.py$", dir_entry.name.lower()):
            py_files.append(dir_entry.name)

    return py_files


def run(config):
    """Import each python file detected in TESTS_LOCATION.

    :param tests_location: <str> Path to directory containing .py modules.
    :param log_name: <str> Optional name of log file.
    """
    tests_location = config["tests_location"]
    log_name = config.get("log_name", "test_results.txt")

    sys.path.append(tests_location)

    test_results_log = os.path.join(tests_location, log_name)
    with open(test_results_log, "w+") as test_results:

        for path_to_py_file in _get_py_files(tests_location):

            py_file = os.path.splitext(path_to_py_file)[0]
            test_module = importlib.import_module(
                py_file.replace("\\", "/"))

            # from here you have access to your test module
            test_results.write(
                "\tContents of {} module:\n".format(path_to_py_file))

            test_case = test_module.Test()
            test_results.write(pformat(dir(test_case)))

            # cant figure out how to get test results here
            results = test_case
            test_results.write(str(results))

            print("\tresults:\n")
            print(pformat(results))

    sys.path.remove(tests_location)

    return test_results


# load config from config.txt
config_dict = load_config()
# run unit test launcher
test_results_log = run(config_dict)

# exit Touch Designer, with optional callback
callback_ = os.startfile
# exit(callback_, test_results_log.name)
