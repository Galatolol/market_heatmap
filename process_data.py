from pandas import DataFrame, isna
from numpy import nan


def get_cell_value(market, i, j):
    try:
        if i < 0 or j < 0:
            raise IndexError
        return market.iat[i, j]
    except IndexError:
        return nan


def calculate_mean(value1, value2):
    if isna(value1):
        return value2
    if isna(value2):
        return value1
    return (value1 + value2) / 2


def calculate_delta(cell, cell_to_left, cell_below):
    neighbors_mean = calculate_mean(cell_to_left, cell_below)
    return (cell / neighbors_mean - 1) * 100


def calculate_heat_map(market: DataFrame):
    delta_values = 0
    row_num = market.shape[0]
    col_num = market.shape[1]
    a = get_cell_value(market, 0, -1)
    for i in range(0, row_num):
        for j in range(col_num - 1, -1, -1):
            cell = get_cell_value(market, i, j)
            if isna(cell):
                continue

            cell_to_left = get_cell_value(market, i, j - 1)
            cell_below = get_cell_value(market, i + 1, j)
            print(f'{cell}, {cell_to_left}, {cell_below}')
            print(calculate_delta(cell, cell_to_left, cell_below))