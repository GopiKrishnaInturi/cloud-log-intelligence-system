import pandas as pd

def summarize_logs(dataframe: pd.DataFrame):
    return dataframe.groupby("severity").size().reset_index(name="count")