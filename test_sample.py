import unittest
from sample import increment_by_two

class TestSampleMethods(unittest.TestCase):

    def test_increment_by_two(self):
        """
        Test increments
        """
        self.assertEqual(increment_by_two(-2), 0)
        self.assertEqual(increment_by_two(0), 2)
        self.assertEqual(increment_by_two(3), 3)

if __name__ == '__main__':
    unittest.main()
