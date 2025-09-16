import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

hitters = pd.read_csv('weighed_stats/weighted_hitters.csv')
pitchers = pd.read_csv('weighed_stats/weighted_pitchers.csv')

# SCALER TO CHANGE DATA INTO 0-1 FORMAT
scaler = MinMaxScaler()

# HITTERS STATS
contact_stats = ['on_base_percent', 'batting_avg', 'z_swing_miss_percent', 'k_percent']
power_stats = ['slg_percent', 'woba','hard_hit_percent', 'home_run']

# COPY THE DATA AND CALL SCALER ON IT 
hitters_norm = hitters.copy()
hitters_norm[contact_stats + power_stats] = scaler.fit_transform(hitters[contact_stats + power_stats])

# SINCE LOWER IS BETTER, WE HAVE TO REVERSE THESE STATS
hitters_norm['k_percent'] = 1 - hitters_norm['k_percent']
hitters_norm['z_swing_miss_percent'] = 1 - hitters_norm['z_swing_miss_percent']

# VALUE HITTERS BY CONTACT
hitters_norm['contact_score'] = (
    hitters_norm['on_base_percent'] * 0.3 +
    hitters_norm['batting_avg'] * 0.3 +
    hitters_norm['z_swing_miss_percent'] * 0.2 +
    hitters_norm['k_percent'] * 0.2
)

# VALUE HITTERS BY POWER
hitters_norm['power_score'] = (
    hitters_norm['slg_percent'] * 0.3 +
    hitters_norm['woba'] * 0.3 + 
    hitters_norm['hard_hit_percent'] * 0.2 +
    hitters_norm['home_run'] * 0.2 
)

top_contact = hitters_norm.sort_values('contact_score', ascending=False)
top_power = hitters_norm.sort_values('power_score', ascending=False)

# SAVE IT TO A CSV FILE
hitters_norm.to_csv('ranked_free_agents/ranked_hitters.csv', index=False)

# STATS TO RANK STRIKEOUT PITCHERS
strikeout_stats = ['k_percent', 'whiff_percent', 'bb_percent', 'xiso']
overall_stats = ['on_base_plus_slg', 'on_base_percent', 'woba', 'hard_hit_percent']

# COPY PITCHERS AND SCALE THE STATS
pitchers_norm = pitchers.copy()
pitchers_norm[strikeout_stats + overall_stats] = scaler.fit_transform(pitchers[strikeout_stats + overall_stats])

# LOWER IS BETTER HAVE TO FLIP THEM
pitchers_norm['bb_percent'] = 1 - pitchers_norm['bb_percent']
pitchers_norm['xiso'] = 1 - pitchers_norm['xiso']
pitchers_norm['on_base_plus_slg'] = 1 - pitchers_norm['on_base_plus_slg']
pitchers_norm['on_base_percent'] = 1 - pitchers_norm['on_base_percent']
pitchers_norm['hard_hit_percent'] =  1 - pitchers_norm['hard_hit_percent']
pitchers_norm['woba'] = 1 - pitchers_norm['woba']

# RANK PITCHERS BY STRIKEOUT ABILITY
pitchers_norm['strikeout_score'] = (
    pitchers_norm['k_percent'] * 0.3 +
    pitchers_norm['whiff_percent'] * 0.3 +
    pitchers_norm['bb_percent'] * 0.2 +
    pitchers_norm['xiso'] * 0.2
)


# RANK PITCHERS OVERALL
pitchers_norm['overall_score'] = (
    pitchers_norm['on_base_plus_slg'] * 0.3 +
    pitchers_norm['on_base_percent'] * 0.3 + 
    pitchers_norm['woba'] * 0.2 +
    pitchers_norm['hard_hit_percent'] * 0.2
)

top_strikeout = pitchers_norm.sort_values('strikeout_score', ascending=False)
top_overall = pitchers_norm.sort_values('overall_score', ascending=False)

pitchers_norm.to_csv('ranked_free_agents/ranked_pitchers.csv', index=False)


