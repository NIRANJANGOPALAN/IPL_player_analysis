import pandas as pd

# Read the HTML file
html_file = 'players_stats_table.html'
tables = pd.read_html(html_file)

# Assuming there's only one table in the HTML file
table = tables[0]

# Print the table
print(table)
# table.to_csv('output.csv', index=False)