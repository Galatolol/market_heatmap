## About

Tool to generate heatmaps of stock markets from 18xx games.
Inspired by the 1849's market heatmap (see `examples/source_picture.jpg`).

The formula for Δ% (relative delta) is as follows:

_Δ% = (N / avg(N_l, N_b) - 1) * 100_

Where _N_0_ is value of a given cell, _N_l_ is value of the cell to the left and _N_b_ is value of the cell below.

When calculating _Δ%_ "from left" and "from below", _N_b_ and _N_l_ are ignored, respectively.

## Use

Run python3:

`python3`

Import the main function:

`from main import generate_market_heatmaps`

Execute the function:

`generate_market_heatmaps(market_path='data/1830_market.html')`

## Parameters

`market_path` - path to the file representing the market. Either `hml` or `csv`.
`html` file is market representation extracted from the Market tab in a game on https://18xx.games.
In Inspect mode right-click on the `div` that contains the whole market (but not the legend below it)
and select `Copy` -> `Inner HTML` (or equivalent).
Then format it by pasting in https://webformatter.com/html and save as `.html` file.

**Important:** The above parameter must be provided

`output_path` - path in which to save generated heatmap images. `'output/heatmap.png'` by default.

`show_market` - whether to generate the heatmap of the market, keeping the raw values.
`False` by default

`delta_from_left_and_below` - whether tho generate the heatmap combinging values bogh to the left and below.
`True` by default

`delta_from_left` - whether to generate the heatmap ignoring values of cells below
(i.e. typically when paying out).
`False` by default

`delta_from_below` - whether to generate the heatmap ignoring values of cells to the left
(i.e. typically when being sold out).
`False` by default

**Important:** at least on of the four above parameters must be `True`.

`vmax` - threshold after which every value will have the same color.
Smaller it is, less precisely the heatmap differentiates between large values (i.e. they are of the same color),
but more precisely between smaller ones. Ignored for the heatmap that shows the raw market values.
`51` by default. `None` if you want to ignore it (then `vmax` is the largest value)

`color_scheme` - in what colors heatmaps are colored. `'gist_ncar'` by default.
See https://matplotlib.org/stable/tutorials/colors/colormaps.html and https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f.
For a monochrome scheme I recommend `Oranges`; for a classic "from blue to red": `jet`.
`gist_ncar` is used by default as it is specifically suited to show small differences in several bands of values

## Examples

In `examples` directory you can find some example heatmaps generated with different settings.

## First time use

Install the required Python packages:

`pip3 install -r requirements.txt`