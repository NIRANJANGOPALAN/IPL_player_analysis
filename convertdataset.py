import pandas as pd


dc = 'Delhi_capitals_2024.html'
kkr = 'KKR_2024.html'
fullStats = 'players_stats_table.html'
teamRecord = 'teamRecord.html'

dc_batting_2024 = './Delhi_Capitals/batting2024.html'
dc_bowling_2024 = './Delhi_Capitals/bowling_2024.html'

kkr_batting_2024 = "./Kolkata/batitng_2024.html"
# Read the HTML file
html_file = kkr_batting_2024
tables = pd.read_html(html_file)

# Assuming there's only one table in the HTML file
table = tables[0]

# Print the table
print(table)
# table.to_csv('kkr_batting_2024_players_records.csv', index=False)