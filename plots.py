from pandas import DataFrame
import seaborn as sns


def generate_plot(data: DataFrame, ax, title: str, vmax: int, color_scheme: str):
    sns.heatmap(data, annot=True, vmax=vmax, fmt='g', ax=ax, cmap=color_scheme)
    ax.set_title(title)
    ax.set_facecolor('gray')