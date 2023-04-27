import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="7dbs", user='williamcrupi', password='Lenn0n6969!', host='127.0.0.1', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")
cursor.execute("select * from cities")
print(cursor.fetchall())

#Closing the connection
conn.close()
