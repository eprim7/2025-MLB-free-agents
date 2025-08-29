import pandas as pd

free_agents_hitters = pd.read_csv('free_agents/free_agents_hitters.csv')

free_agents_hitters.to_csv('free_agents/free_agents_hitters.csv', index=False)

free_agents_hitters['Name'] = free_agents_hitters['Name'].str.strip().str.lower()

# Merge 2025 free agent hitters
hitters_stats = pd.read_csv('every_player_stat/2025_hitters_stats.csv')
hitters_stats['Name'] = hitters_stats['Name'].str.strip().str.lower()

merged = free_agents_hitters.merge(hitters_stats, how='left', on='Name')
merged.to_csv('uncleaned_stats/2025_free_agent_hitters_stats.csv', index=False)


# Merge 2024 free agent hitters
free_agents_hitters_stats_2024 = pd.read_csv('every_player_stat/2024_hitters_stats.csv') 
free_agents_hitters_stats_2024['Name'] = free_agents_hitters_stats_2024['Name'].str.strip().str.lower()

merged = free_agents_hitters.merge(free_agents_hitters_stats_2024, how='left', on='Name')
merged.to_csv('uncleaned_stats/2024_free_agent_hitters_stats.csv', index=False)

# Merge 2023 free agent hitters
free_agents_hitters_stats_2023 = pd.read_csv('every_player_stat/2023_hitters_stats.csv')
free_agents_hitters_stats_2023['Name'] = free_agents_hitters_stats_2023['Name'].str.strip().str.lower()

merged = free_agents_hitters.merge(free_agents_hitters_stats_2023, how='left', on='Name')
merged.to_csv('uncleaned_stats/2023_free_agent_hitters_stats.csv', index=False)


