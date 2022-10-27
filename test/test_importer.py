import unittest
from pandas.testing import assert_frame_equal
from pandas import DataFrame

from importer import import_csv_market

class TestImporter(unittest.TestCase):
    MARKET_CSV_PATH = 'test_market.csv'
    MARKET = [
        [100, 110, 120, 130],
        [90, 100],
        [80]
    ]

    def test_import_csv_market(self):
        result = import_csv_market(self.MARKET_CSV_PATH)
        assert_frame_equal(result, DataFrame(self.MARKET))