import seaborn as sns
import matplotlib.pyplot as plt
from pandas import isna


from process_data import calculate_delta_map
from utils import import_csv_market
from plots import generate_plot


DELTA_TYPES = ['from_left', 'from_below', 'from_left_and_below']


def generate_market_heatmaps(
        img_market_path: str = '',
        csv_market_path: str = '',
        show_market: bool = True,
        delta_from_left: bool = True,
        delta_from_below: bool = True,
        delta_from_left_and_below: bool = True
):
    GAME = '1894'
    MARKET_PATH = f'data/{GAME}_market.csv'

    market = import_csv_market(MARKET_PATH)

    fig, axs = plt.subplots(4)

    if show_market:
        generate_plot(market, axs[0], 'Market')
    if delta_from_left:
        deltas = calculate_delta_map(market, from_left=True)
        generate_plot(deltas, axs[1], 'From left [Δ%]')
    if delta_from_below:
        deltas = calculate_delta_map(market, from_below=True)
        generate_plot(deltas, axs[2], 'From below [Δ%]')
    if delta_from_left_and_below:
        deltas = calculate_delta_map(market, from_left=True, from_below=True)
        generate_plot(deltas, axs[3], 'From left and below combined [Δ%]')

    plt.show()



if __name__ == '__main__':
    GAME = '1894'
    CSV_MARKET_PATH = f'data/{GAME}_market.csv'

    generate_market_heatmaps(csv_market_path=CSV_MARKET_PATH)

    # a = DataFrame(deltas_from_left_and_below)
    # ax = plt.axes()
    # heatmap = sns.heatmap(a, annot=True, ax=ax, cmap='Oranges')
    # plt.show()
    # a = 2


