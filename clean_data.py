import pandas as pd

# clean all the data for the hitters

# 2023 hitters
free_agents_hitters_2023_stats = pd.read_csv('uncleaned_stats/2023_free_agent_hitters_stats.csv')
free_agents_hitters_2023_stats = free_agents_hitters_2023_stats.fillna(0)
free_agents_hitters_2023_stats.to_csv('cleaned_stats/2023_free_agent_hitters_stats_cleaned.csv')

# 2024 hitters
free_agents_hitters_2024_stats = pd.read_csv('uncleaned_stats/2024_free_agent_hitters_stats.csv')
free_agents_hitters_2024_stats = free_agents_hitters_2024_stats.fillna(0)
free_agents_hitters_2024_stats.to_csv('cleaned_stats/2024_free_agent_hitters_stats_cleaned.csv')

# 2025 hitters
free_agents_hitters_2025_stats = pd.read_csv('2025_free_agent_hitters_stats.csv')
free_agents_hitters_2025_stats = free_agents_hitters_2025_stats.fillna(0)
free_agents_hitters_2025_stats.to_csv('cleaned_stats/2025_free_agent_hitters_stats_cleaned.csv')


# clean all the data for the pitchers

# 2023 pitchers
free_agents_pitcher_2023_stats = pd.read_csv('uncleaned_stats/2023_free_agent_pitchers_stats.csv')
free_agents_pitcher_2023_stats = free_agents_pitcher_2023_stats.fillna(0)
free_agents_pitcher_2023_stats.to_csv('cleaned_stats/2023_free_agent_pitchers_stats_cleaned.csv')

# 2024 pitchers
free_agents_pitcher_2024_stats = pd.read_csv('uncleaned_stats/2024_free_agent_pitchers_stats.csv')
free_agents_pitcher_2024_stats = free_agents_pitcher_2024_stats.fillna(0)
free_agents_pitcher_2024_stats.to_csv('cleaned_stats/2024_free_agent_pitchers_stats_cleaned.csv')

# 2025 pitchers
free_agents_pitcher_2025_stats = pd.read_csv('uncleaned_stats/2025_free_agent_pitchers_stats.csv')
free_agents_pitcher_2025_stats = free_agents_pitcher_2025_stats.fillna(0)
free_agents_pitcher_2025_stats.to_csv('cleaned_stats/2025_free_agent_pitchers_stats_cleaned.csv')