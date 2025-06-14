import os
import pandas as pd


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(BASE_DIR, "assets", "data", "StudentPerformanceFactors.csv")
df = pd.read_csv(data_path, sep=";")
