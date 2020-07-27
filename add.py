import sqlite3
import socket

connect=sqlite3.connect("Bank.db")
cursor=connect.cursor()

cursor.execute("INSERT INTO banker VALUES(1,'selin','selin@banka.com')")
cursor.execute("INSERT INTO banker VALUES(2,'ali','ali@banka.com')")

cursor.execute("INSERT INTO banker VALUES(3,'pelin','pelin@banka.com')")

cursor.execute("INSERT INTO customer VALUES(010202,'veli','karanfil','istanbul')")
                           

cursor.execute("INSERT INTO customer VALUES(010302,'derya','kara','izmir')")
                           

cursor.execute("INSERT INTO customer VALUES(010702,'ahmet','limon','bursa')")
                           

cursor.execute("INSERT INTO branch VALUES(1,'merkez','mersin',1000000)")
                           

cursor.execute("INSERT INTO branch VALUES(15,'karatay','konya',2000000)")
                           

cursor.execute("INSERT INTO branch VALUES(3,'kemeraltı','antalya',3000000)")
                          

cursor.execute("INSERT INTO loan VALUES(1,10000,1)")
                           


cursor.execute("INSERT INTO loan VALUES(23,20000,15)")
                           

cursor.execute("INSERT INTO credit_card VALUES(312345,500,15/03/20)")

cursor.execute("INSERT INTO credit_card VALUES(389345,15000,25/08/20)")

cursor.execute("INSERT INTO account VALUES(41238445,5300,'euro')")

cursor.execute("INSERT INTO account VALUES(21236449,5300,'sterlin')")
connect.commit()
connect.close()
