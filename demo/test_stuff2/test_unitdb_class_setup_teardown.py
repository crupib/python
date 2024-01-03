import unitdb_class  as ue
db = None

def setup_module(module):
   print()
   print("Inside setup")
   global db
   db = ue.Database()

def teardown_module(module):
   print()
   print("Inside teardown")
   db.close_connection()

def test_db_case_euro():
   print()
   db = ue.Database()
   val = db.get_data("euro")
   assert val == "euro"
def test_db_case_dollar():
   print()
   db = ue.Database()
   val = db.get_data("dollar")
   assert val == "dollar"
