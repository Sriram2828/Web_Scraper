# Necessary libraries and packages
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Specified the url of the website we want to scrape
web_url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"
result = requests.get(web_url)

# To get the HTML source code of the website using beautifulsoup package
source = BeautifulSoup(result.text, "html.parser")


# Find the table tag in the source code to scrape the data
table = source.find_all('table')[1]

# To grab only the title tag in the table tag
head = table.find_all('th')


# To grab the text inside the title tag
table_title = [title.text.strip() for title in head]

# Create a data frame using pandas to store the text inside the title tag
df = pd.DataFrame(columns=table_title)

# To grab the table_row tag in the table tag
column_data = table.find_all('tr')
# Loop through the table_row tag to grab each data in the table_data tag
for row in column_data[1:]:
    row_data = row.find_all('td')
    separate_row_data = [data.text.strip() for data in row_data]

    # To append each row of data inside the data frame
    length = len(df)
    df.loc[length] = separate_row_data

# Export the data frame to a CSV file
df.to_csv(r'path to the dir\ file_name.csv', index=False)

