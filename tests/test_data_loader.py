import pandas as pd
from titanic_analysis.data_loader import load_titanic_data
import os

def test_load_titanic_data():
    print("Current working directory:", os.getcwd())
    df = load_titanic_data("../../data/titanic.csv")  # Adjust the path if necessary
    assert isinstance(df, pd.DataFrame), "The returned object should be a DataFrame"
    assert not df.empty, "The DataFrame should not be empty"
