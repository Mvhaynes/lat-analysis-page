# Conversion of CSV file to HTML for webpage

import pandas as pd

# Load csv file
csv = 'Resources/cities.csv'
loaded = pd.read_csv(csv)

# Convert to HTML and save
cities_html = loaded.to_html('Resources/cities.html')


