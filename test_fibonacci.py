import unittest
from fibonacci import fibonacci

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_0(self):
        self.assertEqual(fibonacci(0), 0)

    def test_fibonacci_7(self):
        self.assertEqual(fibonacci(7), 13)

if __name__ == "__main__":
    unittest.main()
