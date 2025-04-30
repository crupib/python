import time
class Database:
   def __init__(self):
       time.sleep(3)

   def get_data(self, query):
       time.sleep(1)
       return query
   def close_connection(self):
       print("\n")
       print("Closing")
       return "Database closed"
