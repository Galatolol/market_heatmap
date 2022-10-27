import matplotlib.pyplot as plt
from pathlib import Path

from process_data import calculate_delta_map
from importer import import_csv_market
from plot import generate_plot


def generate_market_heatmaps(
        market_img_path: str = '',
        market_csv_path: str = '',
        output_path: str = 'output/heatmap.png',
        show_market: bool = False,
        delta_from_left: bool = False,
        delta_from_below: bool = False,
        delta_from_left_and_below: bool = True,
        vmax: int = 51,
        color_scheme: str = 'gist_ncar'
):
    if not market_img_path and not market_csv_path:
        raise ValueError('Market source file must be provided')
    if not any([show_market, delta_from_left, delta_from_below, delta_from_left_and_below]):
        raise ValueError('At least one of show_market, delta_from_left, delta_from_below and delta_from_left_and_below must be True')

    market = import_csv_market(market_csv_path)

    sublots_number = sum([show_market, delta_from_left, delta_from_below, delta_from_left_and_below])
    fig, axs = plt.subplots(sublots_number)

    i = 0
    if show_market:
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(market, ax, 'Market', None, color_scheme)
        i += 1
    if delta_from_left:
        deltas = calculate_delta_map(market, from_left=True)
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(deltas, ax, 'From left [Δ%]', vmax, color_scheme)
        i += 1
    if delta_from_below:
        deltas = calculate_delta_map(market, from_below=True)
        generate_plot(deltas, ax, 'From below [Δ%]', vmax, color_scheme)
        i += 1
    if delta_from_left_and_below:
        deltas = calculate_delta_map(market, from_left=True, from_below=True)
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(deltas, ax, 'From left and below combined [Δ%]', vmax, color_scheme)
        i += 1

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(f'{output_path}')


if __name__ == '__main__':
    market_csv_path = f'data/1894_market.csv'

    generate_market_heatmaps(market_csv_path=market_csv_path, show_market=True, delta_from_left_and_below=True, color_scheme='gist_ncar')

