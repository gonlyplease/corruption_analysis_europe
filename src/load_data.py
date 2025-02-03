# load data
import pandas as pd


def load_data(path):
    return pd.read_csv(path, index_col=0)
