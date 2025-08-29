import pandas as pd

free_agent_pitchers = pd.read_csv('free_agents/free_agents_pitchers.csv')

free_agent_pitchers['Name'] = free_agent_pitchers['Name'].str.strip().str.lower()

# Merge 2025 free agent pitchers
free_agent_pitchers_stats_2025 = pd.read_csv('every_player_stats/2025_pitchers_stats.csv') 
free_agent_pitchers_stats_2025['Name'] = free_agent_pitchers_stats_2025['Name'].str.strip().str.lower()

merged = free_agent_pitchers.merge(free_agent_pitchers_stats_2025, how='left', on='Name')
merged.to_csv('uncleaned_stats/2025_free_agent_pitchers_stats.csv', index=False)

# Merge 2024 free agent pitchers
free_agent_pitchers_stats_2024 = pd.read_csv('every_player_stats/2024_pitchers_stats.csv') 
free_agent_pitchers_stats_2024['Name'] = free_agent_pitchers_stats_2024['Name'].str.strip().str.lower()

merged = free_agent_pitchers.merge(free_agent_pitchers_stats_2024, how='left', on='Name')
merged.to_csv('uncleaned_stats/2024_free_agent_pitchers_stats.csv', index=False)

# Merge 2023 free agent pitchers
free_agent_pitchers_stats_2023 = pd.read_csv('every_player_stats/2023_pitchers_stats.csv')
free_agent_pitchers_stats_2023['Name'] = free_agent_pitchers_stats_2023['Name'].str.strip().str.lower()

merged = free_agent_pitchers.merge(free_agent_pitchers_stats_2023, how='left', on='Name')
merged.to_csv('uncleaned_stats/2023_free_agent_pitchers_stats.csv', index=False)
