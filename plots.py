from pandas import DataFrame
import seaborn as sns


def generate_plot(data: DataFrame, ax, title: str):
    sns.heatmap(data, annot=True, fmt='g', ax=ax, cmap='gist_ncar')
    ax.set_title(title)
    ax.set_facecolor('gray')