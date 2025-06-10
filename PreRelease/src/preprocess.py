import pandas as pd

def load_data():
    return pd.read_csv("assets/data/StudentPerformanceFactors.csv", sep=";")
