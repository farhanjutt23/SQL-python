import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",password="Farhan_3015")
db_cu=mydb.cursor()
db_cu.execute("create database Learncoding")
print("this can create")