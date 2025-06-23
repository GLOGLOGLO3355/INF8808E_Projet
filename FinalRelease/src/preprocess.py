import os
import pandas as pd


def load_data():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(
        BASE_DIR, "assets", "data", "StudentPerformanceFactors.csv"
    )
    return pd.read_csv(data_path, sep=";")
