import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from matplotlib import pyplot as plt
from math import floor, ceil, sqrt, exp, log
import requests
import pickle
import time

def get_returns(id):
    r = requests.get("http://egchallenge.tech/marketdata/epoch/" + str(id))
    return pd.DataFrame(r.json())["epoch_return"]

def save_returns_df(df):
    with open("returns_df", "wb") as f:
        pickle.dump(df, f)

def create_returns_df(target_epoch=3500):
    try:
        with open("returns_df", "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        # This will happen the first time we run the program,
        # because the file won't exist yet
        # So we have to download the data and put it in a DataFrame
        ret = {}
        for t in range(target_epoch):
            if (t % 20 == 0):
                print("Downloading returns for epoch " + str(t))
            ret[t] = get_returns(t)
        # When fed a dictionary { colname_i : column_i }, 
        # the DataFrame constructer will create columns 
        # with name colname_i and data column_i
        ret = pd.DataFrame(ret)
        save_returns_df(ret)
        return ret
    
returns_df = create_returns_df()

# We need to transpose the DataFrame first, because statstics are calculated
# on each column, rather than on each row
# The [] operator selects columns by default, so we use it after transposing
returns_df.transpose()[list(range(10))].expanding().sum().plot(
    figsize=[10, 10])
plt.show()
