import unittest
import sys
import os
import unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from runner import Runner

class TestRunner(unittest.TestCase):
    """Testing class for the Runner class"""
    def test_constructor(self):
        """tests Runner's constructor to make sure it works properly"""
        loop = Runner()
        self.assertIsInstance(loop, Runner)

    def test_run(self):
        """tests Runner's main loop to see if it fails upon user use"""
        loop = Runner()
        try:
            loop.run()
        except Exception as e:
            self.fail()

if __name__ == '__main__':
    unittest.main()