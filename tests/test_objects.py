import os
import unittest
from buildnumber import objects, utils

TEST_FILENAME = "test-data/Buildfile"


class BuildnumberTest(unittest.TestCase):
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
        self.assertEquals("0.0.1", bn.get("app1"))
        bn.increment("app1")
        self.assertEquals("0.0.2", bn.get("app1"))
        bn.increment("app1")
        bn.increment("app1")
        self.assertEquals("0.0.4", bn.get("app1"))
        bn.increment("app1", "revision")
        self.assertEquals("0.0.5", bn.get("app1"))
        bn.increment("app1", "minor")
        self.assertEquals("0.1.0", bn.get("app1"))
        bn.increment("app1", "minor")
        self.assertEquals("0.2.0", bn.get("app1"))
        bn.increment("app1", "revision")
        self.assertEquals("0.2.1", bn.get("app1"))
        bn.increment("app1", "revision")
        bn.increment("app1", "revision")
        bn.increment("app1", "revision")
        self.assertEquals("0.2.4", bn.get("app1"))
        bn.increment("app1", "major")
        self.assertEquals("1.0.0", bn.get("app1"))

        app2_version = bn.get("app2")
        self.assertEquals("0.0.2", app2_version)

        app3_version = bn.get("app3")
        self.assertEquals("0.0.3", app3_version)

        app3_version = bn.get("app4")
        self.assertEquals("34", app3_version)

        self.assertEquals("0.0.0", bn.get("no-app"))
