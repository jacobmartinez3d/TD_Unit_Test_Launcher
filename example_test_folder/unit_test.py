import random
import string
import unittest
from pprint import pformat

import td


class Test(unittest.TestCase):

    def test_create_op(self):
        # no name argument
        self.assertIsInstance(
            td.op("/").create(td.containerCOMP), td.containerCOMP)
        # not namespaced
        self.assertIsInstance(
            td.op("/").create(td.containerCOMP), td.containerCOMP)
        self.assertTrue(self._assertWasCreated(
            td.containerCOMP, self._id_generator()))
        # single character name
        self.assertTrue(self._assertWasCreated(
            td.containerCOMP, self._id_generator()))
        # blank name
        self.assertTrue(self._assertWasCreated(td.containerCOMP, ""))
        # rediculously large name
        self.assertTrue(self._assertWasCreated(
            td.containerCOMP, self._id_generator(32767, 32767)))

    def _assertWasCreated(self, class_, name):

        name = self._id_generator()
        td.op("/").create(td.containerCOMP, name)
        ops = [child.name for child in td.op("/").children]

        return name in ops

    @staticmethod
    def _id_generator(min_=1, max_=500, chars=string.ascii_letters):
        """Generate a randome name of randome length."""

        return ''.join(random.choice(chars)
                       for i in range(random.randint(min_, max_)))
