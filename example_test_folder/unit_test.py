"""Example unit test of basic op creation in Touch Designer."""
import random
import string
import unittest
# from pprint import pformat

import td


class Test(unittest.TestCase):
    """Collection of tests related to op creation."""

    def __init__(self):
        super(Test, self).__init__()

    def test_create_op(self):
        # no name argument

        # basic create with no name
        self.assertIsInstance(
            td.op("/").create(td.containerCOMP), td.containerCOMP)
        # class is not namespaced
        self.assertIsInstance(
            td.op("/").create(containerCOMP), td.containerCOMP)

        # validate by searching the root for the op

        # single character name
        self.assertTrue(self._assertWasCreated(
            td.containerCOMP, self._id_generator(1, 1)))
        # blank name
        self.assertTrue(self._assertWasCreated(td.containerCOMP, ""))
        # rediculously large name (using Windows path length limit)
        self.assertTrue(self._assertWasCreated(
            td.containerCOMP, self._id_generator(32767, 32767)))

    def _assertWasCreated(self, name, class_=td.containerCOMP):
        """Return True if a node with the given name exists at the project root.

        :param class_: <cls> td.Op Class type to create.
        :param name: <str> Name of the op to look for.
        """
        name = self._id_generator()
        td.op("/").create(class_, name)
        op_names = [child.name for child in td.op("/").children]

        return name in op_names

    @staticmethod
    def _id_generator(min_=1, max_=500, chars=string.ascii_letters):
        """Generate a random name of random length."""

        return ''.join(random.choice(chars)
                       for i in range(random.randint(min_, max_)))

if __name__ == "__main__":
    unittest.main()
