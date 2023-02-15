import unittest

from date import get_file


class TestMyFunctions(unittest.TestCase):
    def test_read_file_data(self):
        import json
        f = open('fill.json')
        sample_json = json.load(f)
        self.assertEqual(get_file(), sample_json)
        f.close()
