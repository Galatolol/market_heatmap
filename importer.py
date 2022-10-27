from pandas import read_csv, DataFrame
from bs4 import BeautifulSoup
from numpy import nan

def import_csv_market(path: str) -> DataFrame:
    market = read_csv(path, header=None)
    return market


def import_html_market(path: str) -> DataFrame:
    with open(path) as html_file:
        soup = BeautifulSoup(html_file, 'html.parser')
    market = parse_html_txt_market(soup.text)
    return DataFrame(market)


def is_alphanum_or_coma_or_newline(x: str) -> bool:
    if str.isalnum(x) or x == ',' or x == '\n':
        return True
    return False


def nan_or_int(x: str) -> int:
    if x == '\n':
        return nan
    return int(x)


def parse_html_txt_market(html_txt: str) -> list:
    html_txt = ''.join([x for x in html_txt if is_alphanum_or_coma_or_newline(x)])
    html_txt = html_txt.replace('\n\n\n\n\n\n\n', ';').replace('\n\n\n\n\n', ',').strip().replace('\n', '\n,')
    rows = html_txt.split(';')
    market = [[nan_or_int(x) for x in row.split(',') if x] for row in rows]
    return market



