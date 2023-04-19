import unittest
import no1


class FibonacciTest(unittest.TestCase):
    def setUp(self):
        self.func = no1

    def test_limit_10(self):
        self.assertSetEqual(self.func(19), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])