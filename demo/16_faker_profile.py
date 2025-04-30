import openpyxl
from faker import Faker
import pandas as pd
fake = Faker()
profiles = [fake.simple_profile() for i in range(10)]
df = pd.DataFrame(profiles)
pd.set_option('display.max_columns',None)
df.to_excel('Pandas_to_excel_no_index_header.xlsx',index=False, header=True)
#print(df)
