import os
import matplotlib.pyplot as plt

from process_data import calculate_delta_map
from utils import import_csv_market
from plots import generate_plot


def generate_market_heatmaps(
        img_market_path: str = '',
        csv_market_path: str = '',
        output_directory_path: str = 'output',
        show_market: bool = False,
        delta_from_left: bool = False,
        delta_from_below: bool = False,
        delta_from_left_and_below: bool = True
):
    market = import_csv_market(csv_market_path)

    how_many_to_show = sum([show_market, delta_from_left, delta_from_below, delta_from_left_and_below])
    fig, axs = plt.subplots(how_many_to_show)

    i = 0
    if show_market:
        ax = axs if how_many_to_show == 1 else axs[i]
        generate_plot(market, ax, 'Market')
        i += 1
    if delta_from_left:
        deltas = calculate_delta_map(market, from_left=True)
        ax = axs if how_many_to_show == 1 else axs[i]
        generate_plot(deltas, ax, 'From left [Δ%]')
        i += 1
    if delta_from_below:
        deltas = calculate_delta_map(market, from_below=True)
        generate_plot(deltas, ax, 'From below [Δ%]')
        i += 1
    if delta_from_left_and_below:
        deltas = calculate_delta_map(market, from_left=True, from_below=True)
        ax = axs if how_many_to_show == 1 else axs[i]
        generate_plot(deltas, ax, 'From left and below combined [Δ%]')
        i += 1

    if not os.path.isdir(output_directory_path):
        os.makedirs(output_directory_path)
    plt.savefig(f'{output_directory_path}/Heatmap.png')


if __name__ == '__main__':
    GAME = '1894'
    CSV_MARKET_PATH = f'data/{GAME}_market.csv'

    generate_market_heatmaps(csv_market_path=CSV_MARKET_PATH, show_market=True)

