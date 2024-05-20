# %%
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

# %%
df = pd.read_csv("./data/raw/WittData.csv")
df["is_correct"] = df["resp"] == df["corrQuad"]

# %%
dots = pd.read_csv("./data/raw/Witt_Dots.csv")
mean_dots = dots.groupby("currImg", as_index=False)[["x", "y"]].mean()

# Caclulate which quadrant dots are in, seems liek 50 should be the mid-point
conditions = [
    (mean_dots["x"] < 50) & (mean_dots["y"] > 50),
    (mean_dots["x"] > 50) & (mean_dots["y"] > 50),
    (mean_dots["x"] < 50) & (mean_dots["y"] < 50),
    (mean_dots["x"] > 50) & (mean_dots["y"] < 50),
]
values = ["A", "B", "C", "D"]
mean_dots["quadrant"] = np.select(conditions, values)
# %%
df_comb = pd.merge(df, mean_dots, on="currImg", how="left", validate="m:1")
df_comb["calc_is_correct"] = (
    df_comb["quadrant"] == df_comb["resp"]
)  # Calculate correctness based on our recalculated quadrants

df_comb["min_boundary_distance"] = np.minimum(
    (mean_dots["x"] - 50).abs(), (mean_dots["y"] - 50).abs()
)

df_comb.to_parquet("./data/interim/preprocessed_data.parquet")
