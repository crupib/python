from faker import Faker
import numpy as npy
import pandas as pd
fakeDB = Faker()
customerNameList = []
for x in range(100):
    customerNameList.append(fakeDB.name())
customerTransactionList = []
for x in range(100):
   customerTransactionList.append(npy.random.randint(1000,20000))
customerTransactionDF = pd.DataFrame({"Name":customerNameList, "Amount (AED)":customerTransactionList})
print(customerTransactionDF.to_string())
