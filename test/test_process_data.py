import unittest
from pandas.testing import assert_frame_equal
from pandas import DataFrame, isna
from numpy import nan

from process_data import get_cell_value, calculate_delta, calculate_delta_map

class TestImporter(unittest.TestCase):
    MARKET = DataFrame([
        [125, 140, 155, 170],
        [110, 120, 130],
        [100]
    ])


    def test_get_cell_value(self):
        result = get_cell_value(self.MARKET, 0, 2)
        self.assertEqual(result, 155)


    def test_get_cell_value_index_error_too_large(self):
        result = get_cell_value(self.MARKET, 2, 2)
        self.assertTrue(isna(result))


    def test_get_cell_value_index_error_negative(self):
        result = get_cell_value(self.MARKET, 0, -2)
        self.assertTrue(isna(result))


    def test_calculate_delta_1_neighbor(self):
        result = calculate_delta(120, [110])
        self.assertEqual(result, 9)


    def test_calculate_delta_2_neighbors(self):
        result = calculate_delta(155, [140, 130])
        self.assertEqual(result, 15)


    def test_calculate_delta_no_neighbors(self):
        result = calculate_delta(110, [])
        self.assertTrue(isna(result))


    def test_calculate_delta_map_from_left(self):
        expected_result = DataFrame([
            [nan, 12, 11, 10],
            [nan, 9, 8],
            [nan]
        ])
        result = calculate_delta_map(self.MARKET, from_left=True)
        assert_frame_equal(result, expected_result)


    def test_calculate_delta_map_from_below(self):
        expected_result = DataFrame([
            [14, 17, 19, nan],
            [10, nan, nan],
            [nan]
        ])
        result = calculate_delta_map(self.MARKET, from_below=True)
        assert_frame_equal(result, expected_result)


    def test_calculate_delta_map_from_left_and_below(self):
        expected_result = DataFrame([
            [14, 14, 15, 10],
            [10, 9, 8],
            [nan]
        ])
        result = calculate_delta_map(self.MARKET, from_left=True, from_below=True)
        assert_frame_equal(result, expected_result)