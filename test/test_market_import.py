import unittest
from pandas.testing import assert_frame_equal
from pandas import DataFrame
from numpy import nan

from market_import import import_csv_market, import_html_market

class TestImporter(unittest.TestCase):
    MARKET_CSV_PATH = 'test_market.csv'
    MARKET_HTML_PATH = 'test_market.html'
    MARKET = DataFrame([
        [nan, nan, 125, 140, 155, 170],
        [110, 120, 130],
        [nan, 100]
    ])


    def test_import_csv_market(self):
        result = import_csv_market(self.MARKET_CSV_PATH)
        assert_frame_equal(result, self.MARKET)


    def test_import_html_market(self):
        result = import_html_market(self.MARKET_HTML_PATH)
        assert_frame_equal(result, self.MARKET)
