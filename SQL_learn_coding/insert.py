import mysql.connector as mycon

mydb = mycon.connect(
        host="localhost",
        user="root",
        password="Farhan_3015",
        database="Learncoding"
    )
    
db_cu = mydb.cursor()
db_insert="insert into Emp(Roll,Ename ) values (%s,%s)"
db_list=[(20,"Farhan"),(21,"Sajjad"),(22,"Ali Ahmad"),(23,"Rahman")]
db_cu.executemany(db_insert,db_list)
mydb.commit()
print(db_cu.rowcount,"Record insert")
