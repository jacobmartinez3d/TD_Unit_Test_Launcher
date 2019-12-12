"""Example unit test of basic op creation in Touch Designer."""
import random
import string
import unittest
# from pprint import pformat

import td


class TestMain(unittest.TestCase):
    """Collection of tests related to op creation."""

    def test_create_op(self):
        """Test various default Touch Designer op-creation scenarios."""
        # validate by searching the root for the op
        self.assertIsInstance(td.op("/").create(td.containerCOMP), str)
        # single character name
        self.assertTrue(self._assertWasCreated(self._id_generator(1, 1), td.containerCOMP))
        # # rediculously large name (using Windows path length limit)
        self.assertTrue(self._assertWasCreated(self._id_generator(1000, 1000), td.containerCOMP))
        # uncomment below to trigger a failed test result.
        # Don't forget to uncomment the 'print(test_results.failures)' line in unit_test_launcher.py
        # self.assertTrue(False)

    def _assertWasCreated(self, name, class_):
        """Return True if a node with the given name exists at the project root.

        :param class_: <cls> td.Op Class type to create.
        :param name: <str> Name of the op to look for.
        """
        td.op("/").create(class_, name)
        op_names = [child.name for child in td.op("/").children]

        return name in op_names

    @staticmethod
    def _id_generator(min_=1, max_=50, chars=string.ascii_letters):
        """Generate a random name of random length."""

        return ''.join(random.choice(chars) for i in range(random.randint(min_, max_)))


if __name__ == "__main__":
    unittest.main()
