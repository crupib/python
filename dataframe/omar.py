import pandas as pd # library for data analysis
import requests # library to handle requests
from bs4 import BeautifulSoup # library to parse HTML documents

# get the response in the form of html
wikiurl="https://en.wikipedia.org/wiki/List_of_U.S._states_and_territories_by_population#State_and_territory_rankings"
table_class="wikitable sortable jquery-tablesorter"
response=requests.get(wikiurl)
print(response.status_code)
# parse data from the html into a beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')
indiatable=soup.find('table',{'class':"wikitable"})
df=pd.read_html(str(indiatable))
# convert list to dataframe
df=pd.DataFrame(df[0])
print(df)
# drop the unwanted columns
#data = df.drop(["% of Elec. Coll.","% of the total U.S. pop.[d]","Census pop. per seat","Pop. per elec. vote, 2021[c]","House of Reps.[b]","Census population[7][8][a]","Change,2020–2021[7][a]"], axis=1)
#print(data)
#print(df['State or territory']['Census pop. per seat']['20'].where(df['State or territory'] == "California"))
