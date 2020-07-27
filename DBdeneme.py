import sqlite3
import socket

connect=sqlite3.connect("Bank.db")
cursor=connect.cursor()
def banker_table_create():
    cursor.execute(
        "Create table if not exists banker("+
        "banker_id INT NOT NULL UNIQUE,"+
        "banker_name Char(15) NOT NULL,"+
        "banker_mail Char(15) NOT NULL,"+
        "PRIMARY KEY(banker_id))")
    connect.commit()

def branch_table_create():
        cursor.execute(
            "Create table if not exists branch(" +
            "branch_id INT NOT NULL UNIQUE," +
            "branch_city Char(15) NOT NULL," +
            "branch_name Char(15) NOT NULL ," +
            "assets INT NOT NULL," +
            "PRIMARY KEY(branch_id))")
        connect.commit()


def credit_card_table_create():
    cursor.execute(
        "Create table if not exists credit_card(" +
        "credit_card_id INT NOT NULL UNIQUE," +
        "expired_date DATE NOT NULL," +
        "lim INT NOT NULL," +
        "PRIMARY KEY(credit_card_id))")
    connect.commit()
def customer_table_create():
    cursor.execute(
        "Create table if not exists customer("+
        "customer_id INT NOT NULL UNIQUE,"+
        "customer_name Char(15) NOT NULL,"+
        "customer_street Char(15) NOT NULL,"+
        "customer_city Char(15) NOT NULL," +
        "PRIMARY KEY(customer_id))")
    connect.commit()
def loan_table_create():
    cursor.execute(
        "Create table if not exists loan(" +
        "loan_id INT NOT NULL UNIQUE," +
        "amount INT NOT NULL," +
        "branch_id INT NOT NULL,"+
        "PRIMARY KEY(loan_id)," +
        "FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON UPDATE CASCADE)") 
    connect.commit()
def account_table_create():
    cursor.execute(
        "Create table if not exists account("+
        "account_id INT NOT NULL UNIQUE,"+
        "balance INT NOT NULL,"+
        "category Char(15) NOT NULL,"+
        "PRIMARY KEY(account_id))")
    connect.commit()
def loan_customer_table_create():
    cursor.execute(
        "Create table if not exists loan_customer(" +
        "loan_id INT NOT NULL," +
        "customer_id INT NOT NULL," +
        "PRIMARY KEY(loan_id,customer_id)," +
        "FOREIGN KEY(loan_id) REFERENCES loan(loan_id) ON UPDATE CASCADE, " +
        "FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE )")
    connect.commit()

def customer_credit_card_account():
    cursor.execute(
        "Create table if not exists customer_credit_card_account(" +
        "customer_id INT NOT NULL," +
        "credit_card_id INT NOT NULL," +
        "account_id INT NOT NULL," +
        "PRIMARY KEY(customer_id,credit_card_id,account_id)," +
        "FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE, " +
        "FOREIGN KEY(credit_card_id) REFERENCES credit_card(credit_card_id) ON UPDATE CASCADE,  " +
        "FOREIGN KEY(account_id) REFERENCES account(account_id) ON UPDATE CASCADE)")
    connect.commit()

def banker_customer_branch():
    cursor.execute(
        "Create table if not exists banker_customer_branch(" +
        "banker_id INT NOT NULL," +
        "customer_id INT NOT NULL," +
        "branch_id INT NOT NULL," +
        "PRIMARY KEY(banker_id,customer_id,branch_id)," +
        "FOREIGN KEY(banker_id) REFERENCES banker(banker_id) ON UPDATE CASCADE, " +
        "FOREIGN KEY(customer_id) REFERENCES customer(customer_id) ON UPDATE CASCADE, " +
        "FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON UPDATE CASCADE)")
    connect.commit()    



    


banker_table_create()
branch_table_create()
credit_card_table_create()
customer_table_create()
loan_table_create()
account_table_create()
loan_customer_table_create()
banker_customer_branch()

connect.close()
