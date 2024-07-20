import mysql.connector as mycon

mydb = mycon.connect(
        host="localhost",
        user="root",
        password="Farhan_3015",
        database="Learncoding"
    )
    
db_cu = mydb.cursor()
db_cu.execute("SHOW TABLES")
    
for i in db_cu:
     print(i)
