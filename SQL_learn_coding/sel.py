import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",password="Farhan_3015")
db_cu=mydb.cursor()
db_cu.execute("select * from Learncoding.Emp")
for db_data in db_cu.fetchall():
  print(db_data)
  


