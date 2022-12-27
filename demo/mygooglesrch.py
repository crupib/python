# pip install google
from googlesearch import search
query = "Mantle NTS Nextechsolutions"
 
for url in search(query):
    print(url)
