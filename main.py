import matplotlib.pyplot as plt
from pathlib import Path

from process_data import calculate_delta_map
from market_import import import_csv_market, import_html_market
from plot import generate_plot


def generate_market_heatmaps(
        market_path: str = '',
        output_path: str = 'output/heatmap.png',
        show_market: bool = False,
        delta_from_left_and_below: bool = True,
        delta_from_left: bool = False,
        delta_from_below: bool = False,
        vmax: int = 51,
        color_scheme: str = 'gist_ncar'
):
    if not market_path:
        raise ValueError('Path to market file must be provided')
    if not any([show_market, delta_from_left, delta_from_below, delta_from_left_and_below]):
        raise ValueError('At least one of show_market, delta_from_left, delta_from_below and delta_from_left_and_below must be True')

    market_path_obj = Path(market_path)
    if market_path_obj.suffix == '.csv':
        market = import_csv_market(market_path)
    elif market_path_obj.suffix == '.html':
        market = import_html_market(market_path)
    else:
        raise ValueError('Market file must be either csv or html')

    sublots_number = sum([show_market, delta_from_left, delta_from_below, delta_from_left_and_below])
    fig, axs = plt.subplots(sublots_number, figsize=(12, 5 * sublots_number))

    i = 0
    if show_market:
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(market, ax, 'Market', None, color_scheme)
        i += 1
    if delta_from_left_and_below:
        deltas = calculate_delta_map(market, from_left=True, from_below=True)
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(deltas, ax, 'From left and below combined [Δ%]', vmax, color_scheme)
        i += 1
    if delta_from_left:
        deltas = calculate_delta_map(market, from_left=True)
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(deltas, ax, 'From left [Δ%]', vmax, color_scheme)
        i += 1
    if delta_from_below:
        deltas = calculate_delta_map(market, from_below=True)
        ax = axs if sublots_number == 1 else axs[i]
        generate_plot(deltas, ax, 'From below [Δ%]', vmax, color_scheme)
        i += 1

    output_path_obj = Path(output_path)
    output_path_obj.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    plt.savefig(output_path, dpi=300)


if __name__ == '__main__':
    market_path = 'data/1871_market.html'

    generate_market_heatmaps(market_path=market_path, show_market=True, delta_from_left_and_below=True,
                             delta_from_left=True, delta_from_below=True, color_scheme='gist_ncar')

