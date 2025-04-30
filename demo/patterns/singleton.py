import pymongo
import psycopg2
class Singleton:
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        print(cls.__instance)
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
class database:
  def __init__(self, db_instance):
     self.db_instance = db_instance
  def setup_mongodb(self,db,col):
     self.mydb = self.db_instance[db]
     self.mycol = mydb[col]
  def query_mongodb(self,title,product):
     myquery = {title:product}
     mydoc = self.mycol.find(myquery)
     for x in mydoc:
         print(x)
  def query_postgres(db,*args):
     cursor = db.cursor()
     for sqlcode in args:
       cursor.execute(sqlcode)
       print(cursor.fetchall())
       print("\n")
  def close_postgresdb(db):
    db.close()

singleton = Singleton()
print("MongoDB Singleton")
singleton.mongoclient=pymongo.MongoClient("mongodb://localhost:27017/")
mydb = singleton.mongoclient["test"]
mymongo = database(mydb)
database.setup_mongodb(mymongo,"test","products")
database.query_mongodb(mymongo,"title","Hammer")
print("\n")
print("Postgresql Singleton\n")
mypostgres = singleton.postgresclient = conn = psycopg2.connect(
   database="7dbs", user='williamcrupi', password='Lenn0n6969!', host='127.0.0.1', port= '5432'
) 
database.query_postgres(mypostgres,"select version()","select * from cities","select * from countries")
database.close_postgresdb(mypostgres)
