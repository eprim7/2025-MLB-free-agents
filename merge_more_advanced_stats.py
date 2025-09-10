import numpy as np
import pandas as pd
import re

# HITTERS
advanced_hitters_2023_stats = pd.read_csv('more_advanced_stats/advanced_stats_hitters_2023.csv')
advanced_hitters_2024_stats = pd.read_csv('more_advanced_stats/advanced_stats_hitters_2024.csv')
advanced_hitters_2025_stats = pd.read_csv('more_advanced_stats/advanced_stats_hitters_2025.csv')

hitters_2023_substats = advanced_hitters_2023_stats[['WAR', 'OPS+', 'Rbat+', 'Player']]
hitters_2024_substats = advanced_hitters_2024_stats[['WAR', 'OPS+', 'Rbat+', 'Player']]
hitters_2025_substats = advanced_hitters_2025_stats[['WAR', 'OPS+', 'Rbat+', 'Player']]

hitters_2023_substats['Player'] = hitters_2023_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()
hitters_2024_substats['Player'] = hitters_2024_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()
hitters_2025_substats['Player'] = hitters_2025_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()

hitters_2023_stats = pd.read_csv('uncleaned_stats/2023_free_agent_hitters_stats.csv')
hitters_2024_stats = pd.read_csv('uncleaned_stats/2024_free_agent_hitters_stats.csv')
hitters_2025_stats = pd.read_csv('uncleaned_stats/2025_free_agent_hitters_stats.csv')

hitters_2023_stats['Name'] = hitters_2023_stats['Name'].str.lower()
hitters_2024_stats['Name'] = hitters_2024_stats['Name'].str.lower()
hitters_2025_stats['Name'] = hitters_2025_stats['Name'].str.lower()

# 2023 Hitters
hitters_2023_merged = pd.merge(hitters_2023_substats, hitters_2023_stats,left_on='Player', right_on='Name')
hitters_2023_merged.to_csv('uncleaned_stats/2023_free_agent_hitters_stats.csv', index=False)

# 2024 Hitters
hitters_2024_merged = pd.merge(hitters_2024_substats, hitters_2024_stats, left_on='Player', right_on='Name')
hitters_2024_merged.to_csv('uncleaned_stats/2024_free_agent_hitters_stats.csv', index=False)

# 2025 Hitters
hitters_2025_merged = pd.merge(hitters_2025_substats, hitters_2024_stats, left_on='Player', right_on='Name')
hitters_2025_merged.to_csv('uncleaned_stats/2025_free_agent_hitters_stats.csv', index=False)


# PITCHERS
advanced_pitchers_2023_stats = pd.read_csv('more_advanced_stats/advanced_stats_pitchers_2023.csv')
advanced_pitchers_2024_stats = pd.read_csv('more_advanced_stats/advanced_stats_pitchers_2024.csv')
advanced_pitchers_2025_stats = pd.read_csv('more_advanced_stats/advanced_stats_pitchers_2025.csv')

pitchers_2023_substats = advanced_pitchers_2023_stats[['WAR', 'ERA+', 'FIP', 'ERA', 'Player']]
pitchers_2024_substats = advanced_pitchers_2024_stats[['WAR', 'ERA+', 'FIP', 'ERA', 'Player']]
pitchers_2025_substats = advanced_pitchers_2025_stats[['WAR', 'ERA+', 'FIP', 'ERA', 'Player']]

pitchers_2023_substats['Player'] = pitchers_2023_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()
pitchers_2024_substats['Player'] = pitchers_2024_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()
pitchers_2025_substats['Player'] = pitchers_2025_substats['Player'].str.replace(r"[#*]", "", regex=True).str.lower()

pitchers_2023_stats = pd.read_csv('uncleaned_stats/2023_free_agent_pitchers_stats.csv')
pitchers_2024_stats = pd.read_csv('uncleaned_stats/2024_free_agent_pitchers_stats.csv')
pitchers_2025_stats = pd.read_csv('uncleaned_stats/2025_free_agent_pitchers_stats.csv')

pitchers_2023_stats['Name'] = pitchers_2023_stats['Name'].str.lower()
pitchers_2024_stats['Name'] = pitchers_2024_stats['Name'].str.lower()
pitchers_2025_stats['Name'] = pitchers_2025_stats['Name'].str.lower()

# 2023 Pitchers
pitchers_2023_merged = pd.merge(pitchers_2023_substats, pitchers_2023_stats,left_on='Player', right_on='Name')
pitchers_2023_merged.to_csv('uncleaned_stats/2023_free_agent_pitchers_stats.csv', index=False)

# 2024 Pitchers
pitchers_2024_merged = pd.merge(pitchers_2024_substats, pitchers_2024_stats, left_on='Player', right_on='Name')
pitchers_2024_merged.to_csv('uncleaned_stats/2024_free_agent_pitchers_stats.csv', index=False)

# 2025 Pitchers
pitchers_2025_merged = pd.merge(pitchers_2025_substats, pitchers_2024_stats, left_on='Player', right_on='Name')
pitchers_2025_merged.to_csv('uncleaned_stats/2025_free_agent_pitchers_stats.csv', index=False)
