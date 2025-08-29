import pandas as pd

columns = []
id_cols = ["Name", "Position", "player_id", "player_age", "year"]
exclude_cols = ["player_id", "player_age", "year"]

# HITTERS
hitters_2025 = pd.read_csv('cleaned_stats/2025_free_agent_hitters_stats_cleaned.csv')
hitters_2024 = pd.read_csv('cleaned_stats/2024_free_agent_hitters_stats_cleaned.csv')
hitters_2023 = pd.read_csv('cleaned_stats/2023_free_agent_hitters_stats_cleaned.csv')

columns = [c for c in hitters_2025.select_dtypes(include="number").columns if c not in exclude_cols]

weighted_hitters = (
    0.5 * hitters_2025[columns] +
    0.3 * hitters_2024[columns] +
    0.2 * hitters_2023[columns]
)

id_cols = [c for c in id_cols if c in hitters_2025.columns]
weighted_hitters = pd.concat([hitters_2025[id_cols], weighted_hitters], axis=1)

weighted_hitters.to_csv('weighed_stats/weighted_hitters.csv', index=False)

# PITCHERS
pitchers_2025 = pd.read_csv('cleaned_stats/2025_free_agent_pitchers_stats_cleaned.csv')
pitchers_2024 = pd.read_csv('cleaned_stats/2024_free_agent_pitchers_stats_cleaned.csv')
pitchers_2023 = pd.read_csv('cleaned_stats/2023_free_agent_pitchers_stats_cleaned.csv')

columns = [c for c in pitchers_2025.select_dtypes(include="number").columns if c not in exclude_cols]

weighted_pitchers = (
    0.5 * pitchers_2025[columns] +
    0.3 * pitchers_2024[columns] +
    0.2 * pitchers_2023[columns]
)

id_cols = [c for c in id_cols if c in pitchers_2025.columns]
weighted_pitchers = pd.concat([pitchers_2025[id_cols], weighted_pitchers], axis=1)

weighted_pitchers.to_csv("weighed_stats/weighted_pitchers.csv", index=False)
