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
def buyItem(crop,farm,user,quantity):
    df = pd.read_csv("farms\\" + "_".join(farm.split(" ")) + ".csv", index_col="crops")
    fd = pd.read_csv("customers.csv", index_col='username')
    df.at[crop, 'quantity'] -= 1
    df.to_csv("farms\\" +"_".join(farm.split(" ")) + ".csv", index = "crops")
    f = open("customers\\" + fd[("name" == user)]['email'] + fd["name" == user]['number']+".csv", "a+")
    f.write(",".join([str(datetime.date), crop, quantity, str(df.at[crop, "price"]), str(fd[])]))
    fd.to_csv("customers.csv", index = False)
    