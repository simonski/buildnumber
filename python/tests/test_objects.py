import os
import unittest
from buildnumber import objects, utils

TEST_FILENAME = "test-data/Buildfile"


class BuildNumberTest(unittest.TestCase):
    @classmethod
    def tearDownClass(self):
        pass

    @classmethod
    def setUpClass(self):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_a_thing(self):
        bn = objects.Buildfile(TEST_FILENAME)
        self.assertEqual("0.0.1", bn.get("app1"))
        bn.increment("app1")
        self.assertEqual("0.0.2", bn.get("app1"))
        bn.increment("app1")
        bn.increment("app1")
        self.assertEqual("0.0.4", bn.get("app1"))
        bn.increment("app1", "revision")
        self.assertEqual("0.0.5", bn.get("app1"))
        bn.increment("app1", "minor")
        self.assertEqual("0.1.0", bn.get("app1"))
        bn.increment("app1", "minor")
        self.assertEqual("0.2.0", bn.get("app1"))
        bn.increment("app1", "revision")
        self.assertEqual("0.2.1", bn.get("app1"))
        bn.increment("app1", "revision")
        bn.increment("app1", "revision")
        bn.increment("app1", "revision")
        self.assertEqual("0.2.4", bn.get("app1"))
        bn.increment("app1", "major")
        self.assertEqual("1.0.0", bn.get("app1"))

        # Test a second app's version numbering.
        self.assertEqual("0.0.2", bn.get("app2"))
        bn.increment("app2")
        self.assertEqual("0.0.3", bn.get("app2"))
        self.assertEqual("1.0.0", bn.get("app1"))  # Check incrementing one app's version doesn't mess up another one.

        # Test a third apps' version numbering.
        self.assertEqual("0.0.3", bn.get("app3"))
        bn.increment("app3", "minor")
        self.assertEqual("0.1.0", bn.get("app3"))
        bn.increment("app3", "major")
        self.assertEqual("1.0.0", bn.get("app3"))
        self.assertEqual("1.0.0", bn.get("app1"))  # Check incrementing one app's version doesn't mess up another one.

        # Test an integer version number.
        self.assertEqual("34", bn.get("app4"))
        bn.increment("app4", "major")
        self.assertEqual("35", bn.get("app4"))
        bn.increment("app4", "minor")
        self.assertEqual("36", bn.get("app4"))
        bn.increment("app4", "revision")
        self.assertEqual("37", bn.get("app4"))
        self.assertEqual("1.0.0", bn.get("app1"))  # Check incrementing one app's version doesn't mess up another one.

        self.assertEqual("0.0.0", bn.get("no-app"))
