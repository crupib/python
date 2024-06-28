import unitdb_class  as ue

def test_db_case_euro():
    db = ue.Database()
    val = db.get_data("euro")
    assert val == "euro"
def test_db_case_dollar():
    db = ue.Database()
    val = db.get_data("dollar")
    assert val == "dollar"
def test_db_case_close_connection():
    db = ue.Database()
    val = db.close_connection()
    assert val == "Database closed"
