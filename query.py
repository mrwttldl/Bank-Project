import sqlite3
import socket

connect=sqlite3.connect("Bank.db")
cursor=connect.cursor()


cursor.execute("Select * from banker;")
sorgu=cursor.fetchall()

print(sorgu)

connect.close()
