import unittest
class MyTest(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)
    def test_example1(self):
        self.assertNotEqual(1,1)

if __name__ == '__main__':
    unittest.main()

