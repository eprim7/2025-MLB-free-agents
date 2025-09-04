import pandas as pd
import numpy as np
import os

# replace rows of all-zeros with NaN
def zero_to_nan(df, cols):
    mask = (df[cols].sum(axis=1) == 0)
    df.loc[mask, cols] = np.nan
    return df

# compute weighted average of numeric columns
def weighted_avg(group, numeric_cols):
    vals = group[numeric_cols].to_numpy()
    weights = group["year_weight"].to_numpy()

    mask = ~np.isnan(vals).all(axis=1)
    vals = vals[mask]
    weights = weights[mask]

    if len(weights) == 0 or weights.sum() == 0:
        return pd.Series([np.nan] * len(numeric_cols), index=numeric_cols)

    weights = weights / weights.sum()
    return pd.Series(np.average(vals, axis=0, weights=weights), index=numeric_cols)

# process hitters or pitchers
def process_free_agents(file_prefix, output_file):

    # LOAD DATA
    df_2025 = pd.read_csv(f'cleaned_stats/2025_free_agent_{file_prefix}_stats_cleaned.csv')
    df_2024 = pd.read_csv(f'cleaned_stats/2024_free_agent_{file_prefix}_stats_cleaned.csv')
    df_2023 = pd.read_csv(f'cleaned_stats/2023_free_agent_{file_prefix}_stats_cleaned.csv')

    # Identify numeric columns (exclude ID fields)
    exclude_cols = ["player_id", "player_age", "year"]
    numeric_cols = [c for c in df_2025.select_dtypes(include="number").columns if c not in exclude_cols]

    # CLEAN ZEROES
    df_2025 = zero_to_nan(df_2025, numeric_cols)
    df_2024 = zero_to_nan(df_2024, numeric_cols)
    df_2023 = zero_to_nan(df_2023, numeric_cols)

    # ADD WEIGHTS
    df_2025["year_weight"] = 0.5
    df_2024["year_weight"] = 0.3
    df_2023["year_weight"] = 0.2

    # STACK YEARS
    all_df = pd.concat([df_2025, df_2024, df_2023])

    # ID columns to merge back
    id_cols = [c for c in ["Name", "Position", "player_id", "player_age"] if c in all_df.columns]

    # Weighted averages per player
    group_key = "Name" if "Name" in all_df.columns else "player_id"
    weighted_df = (
        all_df.groupby(group_key)
        .apply(lambda g: weighted_avg(g, numeric_cols))
        .reset_index()
    )

    # Merge ID info (from 2025 or first available year)
    weighted_df = weighted_df.merge(df_2025[id_cols], on=group_key, how="left")

    # SAVE TO FILE
    os.makedirs("weighed_stats", exist_ok=True)
    weighted_df.to_csv(f"weighed_stats/{output_file}", index=False)
    print(f"Saved {output_file}")

# HITTERS & PITCHERS
process_free_agents("hitters", "weighted_hitters.csv")
process_free_agents("pitchers", "weighted_pitchers.csv")
