import pandas

def import_csv_market(path):
    market = pandas.read_csv(path, header=None)
    return market