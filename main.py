import pandas
from process_data import calculate_heat_map


def import_csv_market(path):
    market = pandas.read_csv(path, header=None)
    return market


if __name__ == '__main__':
    GAME = '1894'
    MARKET_PATH = f'data/{GAME}_market.csv'

    market = import_csv_market(MARKET_PATH)
    calculate_heat_map(market)
