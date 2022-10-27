from pandas import read_csv, DataFrame, isna
from bs4 import BeautifulSoup
from numpy import nan


def import_csv_market(path: str) -> DataFrame:
    market = read_csv(path, header=None)
    return market


def import_html_market(path: str) -> DataFrame:
    HTML_TO_REPLACE = '<div style="position: relative; display: inline-block; padding: 4px; width: 40px; height: 40px; border: 1px solid rgba(0, 0, 0, 0); margin: 0px; vertical-align: top;"></div>'
    HTML_TO_REPLACE_WITH = '\n"nan"\n\n\n'

    with open(path) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')

    adapted_soup = BeautifulSoup(str(soup).replace(HTML_TO_REPLACE, HTML_TO_REPLACE_WITH), 'html.parser')
    market = parse_html_txt_market(adapted_soup.text)

    return DataFrame(market)


def is_alphanum_or_coma_or_newline(x: str) -> bool:
    if str.isalnum(x) or x == ',' or x == '\n':
        return True
    return False


def nan_or_int(x: str) -> int:
    if x in ['\n', 'nan']:
        return nan
    return int(x)


def parse_html_txt_market(html_txt: str) -> list:
    html_txt_junk_removed = ''.join([x for x in html_txt if is_alphanum_or_coma_or_newline(x)])
    html_txt_newlines_replaced = html_txt_junk_removed.replace('\n\n\n\n\n\n\n', ';').replace('\n\n\n\n\n', ',').strip().replace('\n', '\n,')
    rows = html_txt_newlines_replaced.split(';')
    market = [[nan_or_int(x) for x in row.split(',') if x] for row in rows]
    return market



