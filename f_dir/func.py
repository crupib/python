from area_functions import area_rect, area_circle
import unittest
class AFTestCase(unittest.TestCase):
    """Tests for area_functions.py."""
    def setUp(self):
        """Create widths and lengths for all tests."""
        self.width = 3
        self.length = 4
    def test_react_area(self):
       """Test a simple rectangle."""
       area = area_rect(self.width,self.length)
       self.assertEqual(area,12)
def main():
   my_area = area_rect(5,4)
   print(my_area)
   my_area = area_circle(2)
   print(my_area)
if __name__ == '__main__':
   unittest.main()

