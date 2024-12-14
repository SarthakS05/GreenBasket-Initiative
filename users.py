import pandas as pd
import datetime

def add_customer(name, email, number, username, password, address):
    f = open('customers.csv', 'r')
    record = "customers\\" + email + number + ".csv"
    into = False
    for i in f:
        if(",".join([name, email, number, username, password, address]) in i):
            into = True
    if not into:
        f = open('customers.csv', 'a+')
        f.write('\n'+",".join(map(str, [name,email,number,username,password, address])))
    f.close()
    g = open(record, 'w')
    g.write("crop,quantity,price,location,farm,shopping_cart")
    g.close()