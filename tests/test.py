import unittest
from getl import Getl

class TestGetl(unittest.TestCase):

  def test_load_location_history(self):
    getl = Getl('tests/takeout-data')
    getl.load_location_history()

    locations = getl.sql('SELECT * FROM locations;')

    self.assertEqual(len(locations), 2)

    self.assertEqual(locations[0][0], 45.1234567)
    self.assertEqual(locations[0][1], -75.7654321)
    self.assertEqual(locations[0][2], None)
    self.assertEqual(locations[0][3], None)
    self.assertEqual(locations[0][4], None)
    self.assertEqual(locations[0][5], None)
    self.assertEqual(locations[0][6], '2017-07-13 22:40:00')

    self.assertEqual(locations[1][0], -45.1234567)
    self.assertEqual(locations[1][1], 75.7654321)
    self.assertEqual(locations[1][2], 0)
    self.assertEqual(locations[1][3], 42)
    self.assertEqual(locations[1][4], 3.14)
    self.assertEqual(locations[1][5], '[{"type": "STILL", "confidence": 75}, {"type": "ON_FOOT", "confidence": 25}]')
    self.assertEqual(locations[1][6], '2014-05-13 12:53:20')


if __name__ == '__main__':
    unittest.main()
