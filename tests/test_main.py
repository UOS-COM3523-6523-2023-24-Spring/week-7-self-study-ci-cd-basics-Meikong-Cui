import unittest
from main import simple_count, complex_function


class MyTestCase(unittest.TestCase):
    def test_simple_function1(self):
        self.assertEqual(0, simple_count(''))

    def test_simple_function2(self):
        self.assertEqual(5, simple_count('hello'))

    def test_complex_function(self):
        testValue = complex_function()
        flag = testValue in ['behaviour 1', 'behaviour 2']
        msg = "Complex function behaviour outbounds"
        self.assertTrue(flag, msg)
