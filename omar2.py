import pandas as pd # library for data analysis
import requests # library to handle requests
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup # library to parse HTML documents
import unicodedata as normalize

#table_state = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population#State_and_territory_rankings')
#print(f'Total tables: {len(table_state)}')
table_state = pd.read_html('https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population#State_and_territory_rankings',header=1,index_col=0)
#print(len(table_state))
df = table_state[0]
print(df.head())
