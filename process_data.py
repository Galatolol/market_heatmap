from pandas import DataFrame, isna
from numpy import nan
from statistics import mean


def get_cell_value(market: DataFrame, i: int, j: int) -> int:
    try:
        if i < 0 or j < 0:
            raise IndexError
        value = market.iat[i, j]
        return int(value) if not isna(value) else nan
    except IndexError:
        return nan


def calculate_delta(value: int, neighbor_values: list) -> float:
    neighbor_values = [x for x in neighbor_values if not isna(x)]
    if not neighbor_values:
        return nan

    neighbor_values_mean = mean(neighbor_values)
    return round((value / neighbor_values_mean - 1) * 100)


def calculate_delta_map(market: DataFrame, from_left: bool = False, from_below: bool = False) -> DataFrame:
    delta_matrix = []
    row_num = market.shape[0]
    col_num = market.shape[1]

    for i in range(row_num):
        delta_row = []

        for j in range(col_num):
            value = get_cell_value(market, i, j)
            if isna(value):
                continue

            neighbor_values = []
            if from_left:
                neighbor_values.append(get_cell_value(market, i, j - 1))
            if from_below:
                neighbor_values.append(get_cell_value(market, i + 1, j))

            delta = calculate_delta(value, neighbor_values)
            delta_row.append(delta)

        delta_matrix.append(delta_row)

    return DataFrame(delta_matrix)
